(() => {
  // Pagefind owns site-wide full-text search. Catalog browsing is a separate
  // concern and is delegated to DataTables/SearchPanes on the catalog pages.
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

})();
