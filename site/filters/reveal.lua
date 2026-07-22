--- Presentation for semantic sections.
---
--- The corpus marks what a block *is* (`.problem`, `.solution`, `.hint`, and
--- `.occurrence` added by the compiler). This filter decides what that means on
--- screen: everything that would spoil the problem is collapsed behind a
--- summary. Print or exam output would make a different choice here without any
--- card changing.

local labels = {
  ["qual-hint"] = "Hint",
  ["qual-solution"] = "Solution",
  ["qual-occurrence"] = "As it appeared",
}

local function escape(text)
  return text:gsub("&", "&amp;"):gsub("<", "&lt;"):gsub(">", "&gt;")
end

local function summary_for(class, el)
  if class ~= "qual-occurrence" then
    return labels[class]
  end
  local source = el.attributes["source"] or labels[class]
  local locator = el.attributes["locator"]
  if locator then
    return source .. ", problem " .. locator
  end
  return source
end

function Div(el)
  if not FORMAT:match("html") then
    return nil
  end
  for _, class in ipairs(el.classes) do
    if labels[class] then
      local blocks = pandoc.List({
        pandoc.RawBlock(
          "html",
          '<details class="reveal ' .. class .. '"><summary>'
            .. escape(summary_for(class, el))
            .. "</summary>"
        ),
      })
      blocks:extend(el.content)
      blocks:insert(pandoc.RawBlock("html", "</details>"))
      return blocks
    end
  end
  return nil
end
