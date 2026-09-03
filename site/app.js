(() => {
  // One index, two readers: the dialog in the header searches everything, and a
  // listing page searches one kind of card with the facets it offers. Both ask
  // the index for the page of results in front of the reader. They used to be
  // given the whole corpus and asked to filter it themselves.
  const siteRoot = new URL(document.body.dataset.siteRoot || "./", document.baseURI);
  let pagefind;
  const index = async () => {
    if (!pagefind) {
      pagefind = await import(new URL("pagefind/pagefind.js", siteRoot).href);
      await pagefind.options({ baseUrl: siteRoot.pathname });
    }
    return pagefind;
  };

  // A result's title is its source, so a card named for a formula arrives as
  // `$\# G = [G:H]\,\#H$`. Whatever is built from one has to be typeset once it
  // is in the document; MathJax's own pass ran before any of it existed.
  const typesetInto = async (node) => {
    await window.MathJax?.startup?.promise;
    await window.MathJax?.typesetPromise?.([node]);
  };

  const dialog = document.querySelector("#site-search");
  if (dialog) {
    const openButton = document.querySelector("#search-open");
    const closeButton = document.querySelector("#search-close");
    const input = document.querySelector("#site-search-input");
    const results = document.querySelector("#site-search-results");

    const openSearch = async () => {
      dialog.showModal();
      input.focus();
      await index();
    };
    const closeSearch = () => dialog.close();

    let pending = 0;
    const renderResults = async () => {
      const query = input.value.trim();
      const turn = ++pending;
      results.replaceChildren();
      if (query.length < 2) return;
      const search = await (await index()).search(query);
      // A slower earlier query must not overwrite a later one's results.
      if (turn !== pending) return;
      const shown = await Promise.all(search.results.slice(0, 30).map((result) => result.data()));
      if (turn !== pending) return;
      for (const data of shown) {
        const item = document.createElement("li");
        const link = document.createElement("a");
        link.href = data.url;
        link.textContent = data.meta.title || data.url;
        const metadata = document.createElement("span");
        metadata.className = "search-result-meta";
        const kind = document.createElement("span");
        kind.className = "search-result-kind";
        kind.textContent = (data.filters.kind || [])[0] || "";
        const detail = document.createElement("span");
        detail.className = "search-result-detail";
        detail.textContent = data.plain_excerpt ? data.plain_excerpt.slice(0, 120) : "";
        detail.title = decodeURIComponent(data.url);
        metadata.append(kind, detail);
        item.append(link, metadata);
        results.append(item);
      }
      await typesetInto(results);
    };

    openButton.addEventListener("click", openSearch);
    closeButton.addEventListener("click", closeSearch);
    input.addEventListener("input", renderResults);
    dialog.addEventListener("click", (event) => {
      if (event.target === dialog) closeSearch();
    });
    document.addEventListener("keydown", (event) => {
      if (event.key === "/" && !dialog.open) {
        event.preventDefault();
        openSearch();
      }
    });
  }

  // The problem browser and source browser share the same live Pagefind
  // listing machinery. The problem browser adds collection-scoped source order
  // plus random sampling/print; there is no second generator implementation.
  const controls = document.querySelector(".listing-filters");
  const resultList = document.querySelector("#listing-results");
  if (controls && resultList) {
    const listingSearch = document.querySelector("#listing-search");
    const moreButton = document.querySelector("#listing-more");
    const count = document.querySelector("#listing-count");
    const noun = listingSearch.dataset.noun;
    const listingKind = controls.dataset.listingKind;
    const facets = [...document.querySelectorAll("[data-facet]")].map((select) => ({
      axis: select.dataset.facet,
      select,
    }));
    const practiceCount = document.querySelector("#practice-count");
    const sampleButton = document.querySelector("#practice-sample");
    const printButton = document.querySelector("#practice-print");
    const practiceSheet = document.querySelector("#practice-sheet");
    const PAGE = 50;
    const selected = (select) => [...select.selectedOptions].map((option) => option.value);
    const facet = (axis) => facets.find((item) => item.axis === axis)?.select;

    // Filter values are stable ids; names are the labels the build put on the
    // controls. This keeps display naming out of the JavaScript data model.
    const names = new Map();
    for (const { axis, select } of facets) {
      for (const option of select.options) names.set(`${axis}:${option.value}`, option.textContent);
    }
    const named = (axis, values) =>
      (values || []).map((value) => names.get(`${axis}:${value}`) || value);

    let held = [];
    let drawn = 0;
    let turn = 0;
    let collectionIndex;
    let lastSection = "";

    const dataOf = async (result) =>
      typeof result.data === "function" ? result.data() : result;

    const collections = async () => {
      if (!collectionIndex) {
        const response = await fetch(new URL("collection-problems.json", siteRoot));
        if (!response.ok) throw new Error("collection problem index is unavailable");
        collectionIndex = await response.json();
      }
      return collectionIndex;
    };

    const collectionLocator = (data) => data.meta?.collection_locator || "";
    const collectionSourceLabel = (data) =>
      [data.meta?.collection_section || "", collectionLocator(data)].filter(Boolean).join(" · ");

    const row = (data) => {
      const item = document.createElement("li");
      item.className = "listing-row";
      const title = document.createElement("p");
      const link = document.createElement("a");
      link.href = data.url;
      link.textContent = data.meta.title || data.url;
      title.append(link);

      const facetLine = document.createElement("p");
      const values = data.filters || {};
      const locator = collectionLocator(data);
      facetLine.textContent =
        locator ||
        [
          (values.institution || []).join(", "),
          named("source_kind", values.source_kind).join(", "),
          named("area", values.area).join(", "),
          (values.year || []).join(", "),
        ]
          .filter(Boolean)
          .join(" · ") ||
        "Unclassified";

      const aside = document.createElement("p");
      aside.textContent = data.meta.worked || (values.topic || []).join(", ");
      item.append(title, facetLine, aside);
      return item;
    };

    const draw = async () => {
      const mine = turn;
      const page = held.slice(drawn, drawn + PAGE);
      const shown = await Promise.all(page.map(dataOf));
      if (mine !== turn) return;
      const fragment = document.createDocumentFragment();
      for (const data of shown) {
        const section = data.meta?.collection_section || "";
        if (section && section !== lastSection) {
          const heading = document.createElement("li");
          heading.className = "listing-section";
          const title = document.createElement("h2");
          title.textContent = section;
          heading.append(title);
          fragment.append(heading);
        }
        if (section) lastSection = section;
        fragment.append(row(data));
      }
      resultList.append(fragment);
      drawn += page.length;
      moreButton.hidden = drawn >= held.length;
      moreButton.textContent = `Show more (${held.length - drawn} left)`;
      await typesetInto(resultList);
    };

    const matchesCurrentFacets = (data) => {
      const values = data.filters || {};
      for (const { axis, select } of facets) {
        const wanted = selected(select);
        if (!wanted.length) continue;
        const carried = values[axis] || [];
        if (!wanted.some((value) => carried.includes(value))) return false;
      }
      return true;
    };

    const run = async () => {
      const mine = ++turn;
      const term = listingSearch.value.trim();
      const chosenCollections = selected(facet("collection") || { selectedOptions: [] });

      // A single source with no text search has a canonical order that Pagefind
      // cannot infer from per-card relevance. Use the build's appearance index,
      // then apply every other selected facet locally. Searching text switches
      // back to Pagefind relevance, as a search result should.
      if (!term && listingKind === "problem" && chosenCollections.length === 1) {
        const source = (await collections())[chosenCollections[0]];
        const items = source?.items || [];
        held = items.filter(matchesCurrentFacets);
      } else {
        const filters = { kind: listingKind };
        for (const { axis, select } of facets) {
          const values = selected(select);
          if (values.length) filters[axis] = { any: values };
        }
        const options = term ? { filters } : { filters, sort: { listing: "asc" } };
        const search = await (await index()).search(term || null, options);
        if (mine !== turn) return;
        held = search.results;
      }

      if (mine !== turn) return;
      drawn = 0;
      lastSection = "";
      resultList.replaceChildren();
      count.textContent = `${held.length} ${noun}${held.length === 1 ? "" : "s"}`;
      await draw();
    };

    const readUrl = () => {
      const params = new URLSearchParams(location.search);
      listingSearch.value = params.get("q") ?? "";
      for (const { axis, select } of facets) {
        const options = new Set([...select.options].map((option) => option.value));
        const wanted = params.getAll(axis).flatMap((value) =>
          options.has(value) ? [value] : value.split(",").filter(Boolean),
        );
        for (const option of select.options) option.selected = wanted.includes(option.value);
      }
    };

    const writeUrl = ({ sample } = {}) => {
      const url = new URL(location.href);
      if (listingSearch.value) url.searchParams.set("q", listingSearch.value);
      else url.searchParams.delete("q");
      for (const { axis, select } of facets) {
        url.searchParams.delete(axis);
        for (const value of selected(select)) url.searchParams.append(axis, value);
      }
      if (sample === undefined) url.searchParams.delete("sample");
      else url.searchParams.set("sample", String(sample));
      history.replaceState(null, "", url);
    };

    const clearPractice = () => {
      if (!practiceSheet) return;
      practiceSheet.hidden = true;
      practiceSheet.replaceChildren();
      if (printButton) printButton.disabled = true;
    };

    const changed = async () => {
      clearPractice();
      writeUrl();
      await run();
    };

    moreButton.addEventListener("click", draw);
    listingSearch.addEventListener("input", changed);
    for (const { select } of facets) select.addEventListener("change", changed);

    if (practiceSheet && sampleButton && practiceCount && printButton) {
      const statementOf = async (url) => {
        const response = await fetch(url);
        if (!response.ok) return "";
        const parsed = new DOMParser().parseFromString(await response.text(), "text/html");
        return parsed.querySelector(".card-statement")?.innerHTML || "";
      };

      const shuffled = (values) => {
        const copy = values.slice();
        for (let i = copy.length - 1; i > 0; i--) {
          const j = Math.floor(Math.random() * (i + 1));
          [copy[i], copy[j]] = [copy[j], copy[i]];
        }
        return copy;
      };

      const renderSample = async (requested) => {
        const n = Math.max(1, Math.min(100, Number(requested) || 8));
        practiceCount.value = String(n);
        const mine = turn;
        const picked = shuffled(held).slice(0, n);
        const data = await Promise.all(picked.map(dataOf));
        const drawnProblems = await Promise.all(
          data.map(async (item) => ({ item, statement: await statementOf(item.url) })),
        );
        if (mine !== turn) return;

        const heading = document.createElement("h2");
        heading.textContent = "Practice Set";
        practiceSheet.replaceChildren(heading);
        drawnProblems.forEach(({ item, statement }, index) => {
          const question = document.createElement("div");
          question.className = "practice-question";
          const number = document.createElement("div");
          number.className = "practice-number";
          number.textContent = `${index + 1}.`;
          const body = document.createElement("div");
          body.className = "practice-body";
          body.innerHTML = statement;
          const source = document.createElement("div");
          source.className = "practice-source";
          const locator = collectionSourceLabel(item);
          const values = item.filters || {};
          source.textContent =
            locator ||
            [(values.institution || []).join(", "), (values.year || []).join(", ")]
              .filter(Boolean)
              .join(" · ") ||
            "Corpus problem";
          const link = document.createElement("a");
          link.href = item.url;
          link.textContent = item.meta.title || item.url;
          source.append(" · ", link);
          body.append(source);
          question.append(number, body);
          practiceSheet.append(question);
        });
        practiceSheet.hidden = false;
        printButton.disabled = !drawnProblems.length;
        writeUrl({ sample: n });
        await typesetInto(practiceSheet);
      };

      sampleButton.addEventListener("click", () => renderSample(practiceCount.value));
      printButton.addEventListener("click", () => {
        document.body.classList.add("printing-practice");
        window.addEventListener(
          "afterprint",
          () => document.body.classList.remove("printing-practice"),
          { once: true },
        );
        window.print();
      });

      readUrl();
      const initialSample = new URLSearchParams(location.search).get("sample");
      run().then(() => {
        if (initialSample) renderSample(initialSample);
      });
    } else {
      readUrl();
      run();
    }
  }
})();
