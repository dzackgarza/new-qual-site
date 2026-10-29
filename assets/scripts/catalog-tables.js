(() => {
  const problemTable = document.querySelector("#problem-table");
  const sourceTable = document.querySelector("#source-table");
  if (!problemTable && !sourceTable) return;

  const siteRoot = new URL(document.body.dataset.siteRoot || "./", document.baseURI);
  const darkScheme = window.matchMedia("(prefers-color-scheme: dark)");
  const syncLibraryTheme = () =>
    document.documentElement.classList.toggle("dark", darkScheme.matches);
  syncLibraryTheme();
  darkScheme.addEventListener("change", syncLibraryTheme);
  const params = new URLSearchParams(location.search);
  // One value per repeated parameter: vocabulary names such as
  // "University of California, Berkeley" contain commas.
  const values = (key) => params.getAll(key).filter(Boolean);
  const solutionLabel = (value) => {
    const normalized = value.toLowerCase();
    if (normalized === "solved") return "Solved";
    if (normalized === "unsolved") return "Unsolved";
    return value;
  };
  const escapeHtml = (value) =>
    String(value)
      .replaceAll("&", "&amp;")
      .replaceAll("<", "&lt;")
      .replaceAll(">", "&gt;")
      .replaceAll('"', "&quot;");
  const linkRender = (data, type, row) =>
    type === "display"
      ? `<a href="${escapeHtml(row.url)}">${escapeHtml(data)}</a>`
      : data;
  const arrayRender = { _: "[, ]", sp: "[]" };
  const typeset = async (node) => {
    await window.MathJax?.startup?.promise;
    await window.MathJax?.typesetPromise?.([node]);
  };
  const pane = (column, rows) => (rows.length ? { column, rows } : null);
  // SearchPanes silently drops a preselected value that no row carries, so a
  // URL filter that matches nothing would widen to every row. A pane none of
  // whose values occur makes the result empty instead, and the table says why.
  const unmatchedValues = (rows, columns, preSelect) =>
    preSelect
      .filter(({ column, rows: wanted }) => {
        const field = columns[column].data;
        const present = new Set(rows.flatMap((row) => [].concat(row[field] ?? []).map(String)));
        return !wanted.some((value) => present.has(String(value)));
      })
      .flatMap(({ rows: wanted }) => wanted);
  const emptyMessage = (noun, unmatched) =>
    `No ${noun} match the filter ${unmatched.map((value) => `“${value}”`).join(", ")}.`;

  const initProblemTable = async () => {
    const payload = await fetch(new URL("problems.json", siteRoot)).then((response) => response.json());
    const collectionIds = values("collection");
    let rows = payload.rows;
    let collectionMode = false;

    if (collectionIds.length === 1) {
      const collections = await fetch(new URL("collection-problems.json", siteRoot)).then((response) => response.json());
      const source = collections[collectionIds[0]];
      if (source) {
        collectionMode = true;
        rows = source.items.map((item, order) => ({
          id: item.id,
          title: item.meta.title,
          url: item.url,
          source: [item.meta.collection_section, item.meta.collection_locator]
            .filter(Boolean)
            .join(" · "),
          topics: item.filters.topic || [],
          areas: (item.filters.area || []).map((area) => payload.areaNames[area] || area),
          sourceKinds: (item.filters.source_kind || []).map(
            (kind) => payload.sourceKindNames[kind] || kind,
          ),
          institutions: item.filters.institution || [],
          years: item.filters.year || [],
          collections: [source.title],
          section: item.meta.collection_section || "",
          solutionStatus: item.meta.solution_status,
          order,
        }));
      }
    }

    const preSelect = [
      pane(3, values("area").map((area) => payload.areaNames[area] || area)),
      pane(2, values("topic")),
      pane(
        4,
        values("source_kind").map(
          (kind) => payload.sourceKindNames[kind] || kind,
        ),
      ),
      pane(5, values("institution")),
      pane(6, values("year")),
      pane(
        7,
        collectionMode
          ? []
          : collectionIds.map(
              (collection) => payload.collectionNames[collection] || collection,
            ),
      ),
      pane(9, values("solution").map(solutionLabel)),
    ].filter(Boolean);

    const columns = [
        {
          data: "title",
          render: linkRender,
          width: "50%",
          searchPanes: { show: false },
        },
        {
          data: "source",
          width: "20%",
          searchPanes: { show: false },
        },
        {
          data: "topics",
          width: "30%",
          render: arrayRender,
          searchPanes: { orthogonal: "sp", show: true },
        },
        {
          data: "areas",
          visible: false,
          render: arrayRender,
          searchPanes: { orthogonal: "sp", show: true },
        },
        {
          data: "sourceKinds",
          visible: false,
          render: arrayRender,
          searchPanes: { orthogonal: "sp", show: true },
        },
        {
          data: "institutions",
          visible: false,
          render: arrayRender,
          searchPanes: { orthogonal: "sp", show: true },
        },
        {
          data: "years",
          visible: false,
          render: arrayRender,
          searchPanes: { orthogonal: "sp", show: true },
        },
        {
          data: "collections",
          visible: false,
          render: arrayRender,
          searchPanes: { orthogonal: "sp", show: !collectionMode },
        },
        { data: "section", visible: false, searchable: false },
        {
          data: "solutionStatus",
          visible: false,
          searchPanes: { show: true },
        },
        { data: "order", visible: false, searchable: false },
    ];
    // A pane over a column no loaded row fills would list only an empty-table
    // row (collection mode loads one source, which may carry no year).
    columns.forEach((column) => {
      if (!column.searchPanes?.show) return;
      const filled = rows.some((row) => [].concat(row[column.data] ?? []).some((value) => value !== ""));
      if (!filled) column.searchPanes.show = false;
    });
    const unmatched = unmatchedValues(rows, columns, preSelect);
    // A known solution status with no rows is a count of zero, not a bad filter.
    const onlySolution =
      preSelect.length === 1 &&
      preSelect[0].column === 9 &&
      unmatched.every((value) => value === "Solved" || value === "Unsolved");
    const emptyProblems = onlySolution
      ? `No ${unmatched.join(" or ").toLowerCase()} problems.`
      : emptyMessage("problems", unmatched);

    const table = new DataTable(problemTable, {
      data: unmatched.length ? [] : rows,
      language: unmatched.length ? { emptyTable: emptyProblems } : {},
      deferRender: true,
      pageLength: 50,
      lengthMenu: [25, 50, 100],
      search: { search: params.get("q") || "" },
      order: [[10, "asc"]],
      columns,
      rowGroup: collectionMode ? { dataSrc: "section" } : false,
      searchPanes: {
        cascadePanes: true,
        initCollapsed: true,
        orderable: false,
        viewTotal: true,
        preSelect,
      },
      layout: {
        top1: "searchPanes",
        topStart: "pageLength",
        topEnd: "search",
        bottomStart: "info",
        bottomEnd: "paging",
      },
    });
    table.on("draw", () => typeset(problemTable));
    await typeset(problemTable);

    const practiceCount = document.querySelector("#practice-count");
    const sampleButton = document.querySelector("#practice-sample");
    const printButton = document.querySelector("#practice-print");
    const practiceSheet = document.querySelector("#practice-sheet");
    if (!practiceCount || !sampleButton || !printButton || !practiceSheet) return;

    const statementOf = async (url) => {
      const response = await fetch(url);
      if (!response.ok) return "";
      const parsed = new DOMParser().parseFromString(await response.text(), "text/html");
      return parsed.querySelector(".card-statement")?.innerHTML || "";
    };
    const shuffled = (items) => {
      const copy = items.slice();
      for (let i = copy.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [copy[i], copy[j]] = [copy[j], copy[i]];
      }
      return copy;
    };
    const renderSample = async (requested) => {
      const n = Math.max(1, Math.min(100, Number(requested) || 8));
      practiceCount.value = String(n);
      const filtered = table.rows({ search: "applied" }).data().toArray();
      const picked = shuffled(filtered).slice(0, n);
      const drawn = await Promise.all(
        picked.map(async (item) => ({ item, statement: await statementOf(item.url) })),
      );

      const heading = document.createElement("h2");
      heading.textContent = "Practice Set";
      practiceSheet.replaceChildren(heading);
      drawn.forEach(({ item, statement }, index) => {
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
        source.textContent = item.source || "Corpus problem";
        const link = document.createElement("a");
        link.href = item.url;
        link.textContent = item.title;
        source.append(" · ", link);
        body.append(source);
        question.append(number, body);
        practiceSheet.append(question);
      });
      practiceSheet.hidden = false;
      printButton.disabled = !drawn.length;
      await typeset(practiceSheet);
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
    const initialSample = params.get("sample");
    if (initialSample) renderSample(initialSample);
  };

  const initSourceTable = async () => {
    const payload = await fetch(new URL("sources.json", siteRoot)).then((response) => response.json());
    const preSelect = [
      pane(
        1,
        values("source_kind").map(
          (kind) => payload.sourceKindNames[kind] || kind,
        ),
      ),
      pane(2, values("area").map((area) => payload.areaNames[area] || area)),
      pane(3, values("institution")),
      pane(4, values("year")),
    ].filter(Boolean);

    const columns = [
        {
          data: "title",
          render: linkRender,
          searchPanes: { show: false },
        },
        { data: "sourceKind", searchPanes: { show: true } },
        {
          data: "areas",
          render: arrayRender,
          searchPanes: { orthogonal: "sp", show: true },
        },
        { data: "institution", searchPanes: { show: true } },
        { data: "year", searchPanes: { show: true } },
        { data: "worked", searchPanes: { show: false } },
        { data: "order", visible: false, searchable: false },
    ];
    const unmatched = unmatchedValues(payload.rows, columns, preSelect);

    const table = new DataTable(sourceTable, {
      data: unmatched.length ? [] : payload.rows,
      language: unmatched.length ? { emptyTable: emptyMessage("sources", unmatched) } : {},
      deferRender: true,
      pageLength: 50,
      lengthMenu: [25, 50, 100],
      search: { search: params.get("q") || "" },
      order: [[6, "asc"]],
      columns,
      searchPanes: {
        cascadePanes: true,
        initCollapsed: true,
        orderable: false,
        viewTotal: true,
        preSelect,
      },
      layout: {
        top1: "searchPanes",
        topStart: "pageLength",
        topEnd: "search",
        bottomStart: "info",
        bottomEnd: "paging",
      },
    });
    table.on("draw", () => typeset(sourceTable));
  };

  if (problemTable) initProblemTable();
  if (sourceTable) initSourceTable();
})();
