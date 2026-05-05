const fuseOptions = {
  keys: ["title", "author.firstName", "author.lastName"],
  includeScore: true,
  threshold: 0.3,
};

let fuse = null;

window.initializeFuse = function initializeFuse(list) {
  try {
    if (!Array.isArray(list)) {
      throw new Error("Expected list.json to contain an array");
    }

    fuse = new Fuse(list, fuseOptions);
    console.log("Fuse.js initialized successfully with", list.length, "items");
  } catch (error) {
    console.error("Error initializing Fuse.js:", error);
    fuse = null;
  }
};

window.searchFuse = function searchFuse(query) {
  console.log("searchFuse called with query:", query);

  if (!fuse) {
    console.warn("Fuse.js not initialized yet");
    return [];
  }

  if (!query || query.trim() === "") {
    return [];
  }

  try {
    const results = fuse.search(query);
    console.log(`Search results for "${query}":`, results);
    return results;
  } catch (error) {
    console.error("Error during search:", error);
    return [];
  }
};

console.log("Fuse search functions defined and attached to window");