let miniSearch = null;

window.initializeMinisearch = function initializeMinisearch(data) {
  try {
    if (!Array.isArray(data)) {
      throw new Error("Expected list.json to contain an array");
    }

    const dataWithIds = data.map((item, index) => ({
      id: item.id ?? index,
      ...item,
    }));

    miniSearch = new MiniSearch({
      fields: ["title", "author.firstName", "author.lastName"],
      storeFields: ["title", "author"],
      searchOptions: {
        boost: { title: 2 },
        fuzzy: 0.2,
        prefix: true,
        combineWith: "AND",
      },
    });

    miniSearch.addAll(dataWithIds);
    console.log("Minisearch initialized successfully");
  } catch (error) {
    console.error("Error initializing Minisearch:", error);
    miniSearch = null;
  }
};

window.searchMinisearch = function searchMinisearch(searchQuery) {
  if (!miniSearch) {
    console.warn("Minisearch not initialized yet");
    return [];
  }

  if (!searchQuery || searchQuery.trim() === "") {
    return [];
  }

  console.log("Searching for:", searchQuery);

  try {
    const results = miniSearch.search(searchQuery, {
      fuzzy: 0.2,
      prefix: true,
      boost: { title: 2 },
    });

    const transformedResults = results.map((result, index) => ({
      item: {
        title: result.title ?? "",
        author: result.author ?? { firstName: "", lastName: "" },
      },
      refIndex: result.id ?? index,
      score: typeof result.score === "number" ? 1 - result.score : 0,
    }));

    console.log("Transformed results:", transformedResults);
    return transformedResults;
  } catch (error) {
    console.error("Search error:", error);
    return [];
  }
};

console.log("Minisearch search functions defined and attached to window");