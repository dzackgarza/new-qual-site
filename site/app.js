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

  const renderResults = async () => {
    const query = input.value.trim().toLocaleLowerCase();
    results.replaceChildren();
    if (query.length < 2) return;
    const terms = query.split(/\s+/);
    const matches = (await loadIndex())
      .filter((record) => terms.every((term) => record.search.includes(term)))
      .slice(0, 30);
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
      detail.textContent = record.detail;
      metadata.append(kind, detail);
      item.append(link, metadata);
      results.append(item);
    }
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

  // The page says the URL is the query, so it has to be: ?q= seeds the filter on
  // load and tracks it as the reader types, which makes a filtered view
  // shareable and bookmarkable.
  const problemFilter = document.querySelector("#problem-filter");
  if (problemFilter) {
    const applyFilter = () => {
      const terms = problemFilter.value.toLocaleLowerCase().trim().split(/\s+/);
      for (const row of document.querySelectorAll(".problem-row")) {
        row.hidden = !terms.every((term) => row.dataset.search.includes(term));
      }
    };
    problemFilter.value = new URLSearchParams(location.search).get("q") ?? "";
    applyFilter();
    problemFilter.addEventListener("input", () => {
      applyFilter();
      const url = new URL(location.href);
      if (problemFilter.value) {
        url.searchParams.set("q", problemFilter.value);
      } else {
        url.searchParams.delete("q");
      }
      history.replaceState(null, "", url);
    });
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
      link.textContent = heading.textContent;
      item.className = heading.tagName === "H3" ? "toc-subsection" : "";
      item.append(link);
      list.append(item);
    }
    toc.append(label, list);
  }
})();
