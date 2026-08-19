--- Presentation for semantic sections.
---
--- The corpus marks what a block *is* (`.problem`, `.solution`, `.hint`). This
--- filter decides what that means on screen: everything that would spoil the
--- problem is collapsed behind a summary. Print or exam output would make a
--- different choice here without any card changing.

local labels = {
  ["qual-hint"] = "Hint",
  ["qual-solution"] = "Solution",
}

local function escape(text)
  return text:gsub("&", "&amp;"):gsub("<", "&lt;"):gsub(">", "&gt;")
end

local function summary_for(class, _el)
  return labels[class]
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
