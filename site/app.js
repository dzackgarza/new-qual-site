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

  // A listing page: a text box, a select per facet, and the rows the index
  // answers with. The page says which kind of card it lists and which axes it
  // offers; nothing here names a page.
  // ?q= and ?axis= seed the controls on load and track them as the reader
  // works, which makes a filtered view shareable and bookmarkable.
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
    const PAGE = 50;
    const selected = (select) => [...select.selectedOptions].map((option) => option.value);
    // A filter matches on an id and a row shows a name. The controls the page
    // emitted already carry both, so the names are read off them rather than
    // sent a second time: `algebra` is shown as whatever the registry calls it.
    const names = new Map();
    for (const { axis, select } of facets) {
      for (const option of select.options) names.set(`${axis}:${option.value}`, option.textContent);
    }
    const named = (axis, values) => (values || []).map((value) => names.get(`${axis}:${value}`) || value);

    let held = [];
    let drawn = 0;
    let turn = 0;

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
      facetLine.textContent =
        [
          (values.institution || []).join(", "),
          named("source_kind", values.source_kind).join(", "),
          named("area", values.area).join(", "),
          (values.year || []).join(", "),
        ]
          .filter(Boolean)
          .join(" · ") || "Unclassified";
      const aside = document.createElement("p");
      // A collection says how much of it is worked, which no filter can count.
      // A card says what it is about, which its topics already say.
      aside.textContent = data.meta.worked || (values.topic || []).join(", ");
      item.append(title, facetLine, aside);
      return item;
    };

    const draw = async () => {
      const mine = turn;
      const page = held.slice(drawn, drawn + PAGE);
      const shown = await Promise.all(page.map((result) => result.data()));
      if (mine !== turn) return;
      const fragment = document.createDocumentFragment();
      for (const data of shown) fragment.append(row(data));
      resultList.append(fragment);
      drawn += page.length;
      moreButton.hidden = drawn >= held.length;
      moreButton.textContent = `Show more (${held.length - drawn} left)`;
      await typesetInto(resultList);
    };

    const run = async () => {
      const mine = ++turn;
      const filters = { kind: listingKind };
      for (const { axis, select } of facets) {
        const values = selected(select);
        if (values.length) filters[axis] = { any: values };
      }
      const term = listingSearch.value.trim();
      // Browsing and searching want different orders. With nothing typed there
      // is nothing to rank against, so the rows keep the order the listing puts
      // them in; a term ranks them by how well they answer it.
      const options = term ? { filters } : { filters, sort: { listing: "asc" } };
      const search = await (await index()).search(term || null, options);
      if (mine !== turn) return;
      held = search.results;
      drawn = 0;
      resultList.replaceChildren();
      count.textContent = `${held.length} ${noun}${held.length === 1 ? "" : "s"}`;
      await draw();
    };

    moreButton.addEventListener("click", draw);

    const readUrl = () => {
      const params = new URLSearchParams(location.search);
      // No `q` is a real state, not a missing value: it means no term.
      listingSearch.value = params.get("q") ?? "";
      for (const { axis, select } of facets) {
        const wanted = (params.get(axis) || "").split(",").filter(Boolean);
        for (const option of select.options) option.selected = wanted.includes(option.value);
      }
    };
    const writeUrl = () => {
      const url = new URL(location.href);
      if (listingSearch.value) url.searchParams.set("q", listingSearch.value);
      else url.searchParams.delete("q");
      for (const { axis, select } of facets) {
        const values = selected(select);
        if (values.length) url.searchParams.set(axis, values.join(","));
        else url.searchParams.delete(axis);
      }
      history.replaceState(null, "", url);
    };
    const changed = () => {
      writeUrl();
      run();
    };

    readUrl();
    run();
    listingSearch.addEventListener("input", changed);
    for (const { select } of facets) select.addEventListener("change", changed);
  }

  const headings = [
    ...document.querySelectorAll(".page-body h2, .page-body h3"),
  ].filter((heading) => !heading.closest(".relation-group, .card-appearances, footer, .metadata-panel"));
  const toc = document.querySelector("#page-toc");
  if (headings.length && toc) {
    const label = document.createElement("strong");
    label.textContent = "Contents";
    const list = document.createElement("ol");
    for (const heading of headings) {
      if (!heading.id) {
        heading.id = heading.textContent
          .toLocaleLowerCase()
          .replace(/[^\p{Letter}\p{Number}]+/gu, "-")
          .replace(/(^-|-$)/g, "");
      }
      const item = document.createElement("li");
      const link = document.createElement("a");
      link.href = `#${heading.id}`;
      // Copying textContent flattened a heading's mathematics to its source
      // characters, so a card titled with a formula read as raw TeX in the
      // index. Cloning the nodes keeps the math markup, which MathJax then
      // typesets here the same as it does in the heading itself.
      link.append(...heading.cloneNode(true).childNodes);
      item.className = heading.tagName === "H3" ? "toc-subsection" : "";
      item.append(link);
      list.append(item);
    }
    toc.append(label, list);
    // The rail is hidden on narrow viewports, which left long pages with no
    // in-page navigation at all. Asking the layout whether the rail is showing
    // keeps its breakpoint in one place: when it is not, the same headings go
    // above the article as a disclosure, like the mobile wiki nav.
    if (getComputedStyle(toc).display === "none") {
      const narrow = document.createElement("details");
      narrow.className = "page-toc-narrow";
      const summary = document.createElement("summary");
      summary.textContent = "Contents";
      const nav = document.createElement("nav");
      nav.setAttribute("aria-label", "Contents");
      nav.append(list.cloneNode(true));
      narrow.append(summary, nav);
      document.querySelector(".page-body").before(narrow);
    }
  }
})();
