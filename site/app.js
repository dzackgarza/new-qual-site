(() => {
  const dialog = document.querySelector("#site-search");
  const openButton = document.querySelector("#search-open");
  const closeButton = document.querySelector("#search-close");
  const input = document.querySelector("#site-search-input");
  const results = document.querySelector("#site-search-results");
  const searchIndexUrl = new URL(
    document.body.dataset.searchIndex,
    document.baseURI,
  );
  let records;

  const loadIndex = async () => {
    if (!records) {
      const response = await fetch(searchIndexUrl);
      if (!response.ok) {
        throw new Error(`Search index failed: ${response.status}`);
      }
      records = await response.json();
    }
    return records;
  };

  const openSearch = async () => {
    dialog.showModal();
    input.focus();
    await loadIndex();
  };

  const closeSearch = () => dialog.close();

  // Index order is publication order, and every page precedes every card, so an
  // unranked filter answered "sylow" with wiki pages and never reached a Sylow
  // theorem or problem. Rank by where in the record the query landed.
  const rank = (record, query, terms) => {
    const title = record.title.toLocaleLowerCase();
    if (title === query) return 4;
    if (title.startsWith(query)) return 3;
    if (terms.every((term) => title.includes(term))) return 2;
    // A card's kind and id live in `detail`, which makes "P-A4JGH" an id lookup.
    if (record.detail.toLocaleLowerCase().includes(query)) return 1;
    return 0;
  };

  // Every wiki page carries the same constant `detail`, and three of them are
  // titled "Residues", two in one folder: only the path separates those rows.
  // A card keeps its own `detail`, which names a kind its route does not.
  // Only the last two segments are shown: the rail truncates from the right,
  // and the tail is where same-titled pages differ. The rest is the tooltip.
  const locate = (record) => {
    const parts = decodeURIComponent(record.url).replace(/\.html$/, "").split("/");
    return parts.length < 3 ? "" : parts.slice(-2).join(" / ");
  };

  const renderResults = async () => {
    const query = input.value.trim().toLocaleLowerCase();
    results.replaceChildren();
    if (query.length < 2) return;
    const terms = query.split(/\s+/);
    const matches = (await loadIndex())
      .filter((record) => terms.every((term) => record.search.includes(term)))
      .map((record) => ({ record, score: rank(record, query, terms) }))
      .sort(
        (a, b) =>
          b.score - a.score ||
          a.record.title.length - b.record.title.length ||
          a.record.title.localeCompare(b.record.title) ||
          a.record.url.localeCompare(b.record.url),
      )
      .slice(0, 30)
      .map((match) => match.record);
    for (const record of matches) {
      const item = document.createElement("li");
      const link = document.createElement("a");
      link.href = new URL(record.url, searchIndexUrl).href;
      link.textContent = record.title;
      const metadata = document.createElement("span");
      metadata.className = "search-result-meta";
      const kind = document.createElement("span");
      kind.className = "search-result-kind";
      kind.textContent = record.kind;
      const detail = document.createElement("span");
      detail.className = "search-result-detail";
      detail.textContent = locate(record) || record.detail;
      detail.title = decodeURIComponent(record.url);
      metadata.append(kind, detail);
      item.append(link, metadata);
      results.append(item);
    }
    // Titles are stored as their source, so a card named for a formula listed as
    // `$\# G = [G:H]\,\#H$`. MathJax ran before the dialog had any results in it,
    // so the list has to ask for itself.
    await window.MathJax?.typesetPromise?.([results]);
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

  // ?q= seeds the filter on load and tracks it as the reader types,
  // which makes a filtered view shareable and bookmarkable.
  const problemFilter = document.querySelector("#problem-filter");
  if (problemFilter) {
    const facets = ["area", "topic", "institution", "year"].map((axis) => ({
      axis,
      select: document.querySelector(`#problem-${axis}`),
    }));
    const selected = (select) =>
      [...select.selectedOptions].map((option) => option.value);
    const queryValues = (axis) => {
      const value = new URLSearchParams(location.search).get(axis);
      return value ? value.split(",").filter(Boolean) : [];
    };
    const setSelected = (select, values) => {
      for (const option of select.options) option.selected = values.includes(option.value);
    };
    // Topics are free strings and may contain spaces; facet values are joined with `|`.
    const matchesFacet = (row, axis, values) =>
      !values.length || values.every((value) => row.dataset[axis].split("|").includes(value));
    const applyFilter = () => {
      const terms = problemFilter.value.toLocaleLowerCase().trim().split(/\s+/);
      let visible = 0;
      for (const row of document.querySelectorAll(".problem-row")) {
        const matchesSearch = !problemFilter.value.trim() || terms.every((term) => row.dataset.search.includes(term));
        const matchesFacets = facets.every(({ axis, select }) => matchesFacet(row, axis, selected(select)));
        row.hidden = !(matchesSearch && matchesFacets);
        if (!row.hidden) visible += 1;
      }
      const count = document.querySelector("#problem-count");
      if (count) count.textContent = `${visible} problem${visible === 1 ? "" : "s"} shown`;
    };
    // No `q` in the URL is a real state, not a missing value: it means no filter.
    const query = new URLSearchParams(location.search).get("q");
    problemFilter.value = query === null ? "" : query;
    for (const { axis, select } of facets) setSelected(select, queryValues(axis));
    applyFilter();
    const updateUrl = () => {
      applyFilter();
      const url = new URL(location.href);
      if (problemFilter.value) {
        url.searchParams.set("q", problemFilter.value);
      } else {
        url.searchParams.delete("q");
      }
      for (const { axis, select } of facets) {
        const values = selected(select);
        if (values.length) url.searchParams.set(axis, values.join(","));
        else url.searchParams.delete(axis);
      }
      history.replaceState(null, "", url);
    };
    problemFilter.addEventListener("input", updateUrl);
    for (const { select } of facets) select.addEventListener("change", updateUrl);
  }

  const headings = [
    ...document.querySelectorAll(".page-body h2, .page-body h3"),
  ];
  const toc = document.querySelector("#page-toc");
  if (headings.length && toc) {
    const label = document.createElement("strong");
    label.textContent = "On this page";
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
      summary.textContent = "On this page";
      const nav = document.createElement("nav");
      nav.setAttribute("aria-label", "On this page");
      nav.append(list.cloneNode(true));
      narrow.append(summary, nav);
      document.querySelector(".page-body").before(narrow);
    }
  }
})();
