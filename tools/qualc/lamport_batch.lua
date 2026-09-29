-- Apply one Pandoc Lua filter to many Pandoc JSON documents in one process.
--
-- The Pandoc server cannot run Lua filters (it runs in PandocPure), and one
-- `pandoc --lua-filter` process per card costs a Pandoc start per card. `pandoc
-- lua` (https://pandoc.org/MANUAL.html#running-pandoc-as-a-lua-interpreter)
-- runs this script with the `pandoc` module loaded; the filter file defines a
-- global `Pandoc` function, which is called on each document exactly as Pandoc
-- calls it for a filter (https://pandoc.org/lua-filters.html#filters-on-the-whole-document).
--
-- arg[1]: the filter file. arg[2]: the output format the filter sees as FORMAT.
-- stdin: a JSON array of Pandoc JSON documents, each as a string.
-- stdout: a JSON array with one object per document, {"ok": <Pandoc JSON>} or
-- {"error": <message>}.

FORMAT = arg[2]
dofile(arg[1])

local documents = pandoc.json.decode(io.read("a"), false)
local results = {}
for index, text in ipairs(documents) do
  local ok, value = pcall(function()
    local filtered = Pandoc(pandoc.read(text, "json"))
    return pandoc.write(filtered, "json")
  end)
  if ok then
    results[index] = { ok = value }
  else
    results[index] = { error = tostring(value) }
  end
end
io.write(pandoc.json.encode(results))
