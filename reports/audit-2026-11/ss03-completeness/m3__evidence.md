# Evidence: page map, section boundaries, reproduction

## Page map

`PDF page = printed page + 19` throughout the algebraic part of the book. Verified on every page
that shows a folio, e.g. PDF 43 carries `24`, PDF 128 carries `109`, PDF 300 carries `281`,
PDF 336 carries `317`, PDF 383 carries `364`. Roman-numbered front matter ends at PDF 19; printed
page 1 is PDF 20.

Reproduction: `pdftotext -f 1 -l 398 assets/attachments/Stein-Shakarchi-Complex-Analysis.pdf out.txt`,
split on form feed (`\f`); `pages[i-1]` is PDF page `i`. (Done once here; the dump lives in
`.scratch/ss03.txt`, which is a cache and not part of this report.)

## Section boundaries and the anchor used for each

Each row gives the heading as OCR'd on its page, the page it starts on, and the text that closes
the set (the tail-test anchor). "Cards" is the number of files on disk, from the directory listing
and the front matter of `index.md` (206 ids, 206 files; the sets agree exactly).

| set | heading (OCR) | starts | last item's incipit | closes with | cards |
|---|---|---|---|---|---|
| ch1 Exercises | `4 Exercises` | PDF 43 / p. 24 | 26. Suppose f is continuous in a region Ω… | chapter 2 title, PDF 51 / p. 32 | 26 |
| ch2 Exercises | `6 Exercises` | PDF 83 / p. 64 | 15. Suppose f is a non-vanishing continuous function on D… | `7 Problems`, PDF 86 / p. 67 | 15 |
| ch2 Problems | `7 Problems` | PDF 86 / p. 67 | 5.∗ There exists an entire function F… | chapter 3 title, PDF 90 / p. 71 | 5 |
| ch3 Exercises | `8 Exercises` | PDF 122 / p. 103 | 22. Show that there is no holomorphic function f in the unit disc D… | `9 Problems`, PDF 127 / p. 108 | 22 |
| ch3 Problems | `9 Problems` | PDF 127 / p. 108 | 5.∗ Let g(z) = (1/2πi)∫… | chapter 4 title, PDF 130 / p. 111 | 2 |
| ch4 Exercises | `4 Exercises` | PDF 146 / p. 127 | 12. …the following theorem of Hardy. | `5 Problems`, PDF 150 / p. 131 | 12 |
| ch4 Problems | `5 Problems` | PDF 150 / p. 131 | 4.∗ There is a relation between the Paley-Wiener theorem… | chapter 5 title, PDF 153 / p. 134 | 4 |
| ch5 Exercises | `6 Exercises` | PDF 172 / p. 153 | 17. Given two countably infinite sequences… Pringsheim | `7 Problems`, PDF 175 / p. 156 | 17 |
| ch5 Problems | `7 Problems` | PDF 175 / p. 156 | 4.∗ Let F (z) = Σ an z n be an entire function of finite order… | chapter 6 title, PDF 178 / p. 159 | 4 |
| ch6 Exercises | `3 Exercises` | PDF 193 / p. 174 | 17. Let f be an indefinitely differentiable function on R… | `4 Problems`, PDF 198 / p. 179 | 17 |
| ch6 Problems | `4 Problems` | PDF 198 / p. 179 | 4.∗ The functions Qk in the previous problem… | chapter 7 title, PDF 200 / p. 181 | 4 |
| ch7 Exercises | `3 Exercises` | PDF 218 / p. 199 | 12. If pn denotes the nth prime… | `4 Problems`, PDF 222 / p. 203 | 12 |
| ch7 Problems | `4 Problems` | PDF 222 / p. 203 | 4.∗ One can combine ideas from the prime number theorem… | chapter 8 title, PDF 224 / p. 205 | 4 |
| ch8 Exercises | `5 Exercises` | PDF 267 / p. 248 | 24. The elliptic integrals K and K ′ … | `6 Problems`, PDF 273 / p. 254 | 24 |
| ch8 Problems | `6 Problems` | PDF 273 / p. 254 | 9.∗ Gauss found a connection between elliptic integrals… | chapter 9 title, PDF 280 / p. 261 | 9 |
| ch9 Exercises | `3 Exercises` | PDF 297 / p. 278 | 8. Let E4 (τ ) = Σ 1/(n + mτ )4 … | `4 Problems`, PDF 300 / p. 281 | 8 |
| ch9 Problems | `4 Problems` | PDF 300 / p. 281 | 4.∗ Suppose τ is purely imaginary… | chapter 10 title, PDF 302 / p. 283 | 3 |
| ch10 Exercises | `4 Exercises` | PDF 328 / p. 309 | 12. Here we give another identity involving θ4 … | `5 Problems`, PDF 333 / p. 314 | 12 |
| ch10 Problems | `5 Problems` | PDF 333 / p. 314 | 6.∗ Here we will deduce the formula for r8 (n)… | Appendix A title, PDF 337 / p. 318 | 6 |
| App A Problems | `5 Problems` | PDF 360 / p. 341 | 5.∗ The one shortcoming in our derivation … p(n) … | Appendix B title, PDF 363 / p. 344 | 0 |
| App B | — | — | no Exercises/Problems section | Notes and References, PDF 384 / p. 365 | — |

## Numeral-continuity scan

For each set, every line in its page range was tested against `^\s*(\d{1,2})\.?\*?\s*$` and
`^\s*(\d{1,2})\.\s*\*?\s*\S`; the resulting numeral sets are

ch1 EX {1..26}, ch2 EX {1..15}, ch2 PR {1..5}, ch3 EX {1..22}, ch3 PR {1..5}, ch4 EX {1..12},
ch4 PR {1..4}, ch5 EX {1..17}, ch5 PR {1..4}, ch6 EX {1..17}, ch6 PR {1..4}, ch7 EX {1..12},
ch7 PR {1..4}, ch8 EX {1..24}, ch8 PR {1..9}, ch9 EX {1..8}, ch9 PR {1..4}, ch10 EX {1..12},
ch10 PR {1..6}, App A PR {1..5}

with no gap in any of them. Extras picked up by the loose pattern were running heads and folios
(e.g. `27`, `28` on PDF 46–47 are page numbers, `7.` on PDF 86 is the head `7. Problems`), not
items.

## OCR traps that will fool a naive enumeration

These are the places where the numeral is **not** followed by text on the same line, or where the
page break splits an item. Anyone counting with a `^\d+\.\s+[A-Z]` style pattern will report
phantom gaps at exactly the interesting chapters:

* **ch2 exercise 7** — printed as `7.` alone on a line, then `Suppose f : D → C is holomorphic.`
  (PDF 84 / p. 65). A same-line matcher misses item 7 and "finds" a hole.
* **ch8 exercise 19** — printed as `19.` alone on a line, then `Prove that the complex plane slit…`
  (PDF 271 / p. 252). Same failure, and it lands between 18 and 20, i.e. it looks like a genuine
  missing item.
* **ch1 exercises 1–26** — the running head of every odd page in this chapter is `4. Exercises`,
  which the numerals pattern also matches as item `4`; harmless once you compare sets, fatal if you
  count occurrences.
* **ch5 problem 1** — the `[Hint: Use Jensen's formula.]` is on the *next* page (PDF 176 / p. 157)
  from the statement; a page-scoped extraction loses the hint.
* **ch2 exercise 1** — its `[Hint: …]` is interleaved with `Figure 14` by the OCR and comes out
  scrambled between the statement and the display; the hint text itself is intact.
* **ch4 exercise 12 / ch3 problem 22** — the Problems heading is printed on the same page as the
  last exercise (`5 Problems` on p. 131; `9 Problems` on p. 108), so a rule like "exercises end
  where the Problems heading is" must be *inclusive* of that page.

## 3. Alignment sanity check (card text vs printed item blocks)

Counting can only prove that *some* card has each number; it cannot prove that card *n* holds
printed item *n*. A cheap independent check: split each printed set into item blocks by taking the
numeral at line start only when it is the expected next number (so folios and running heads cannot
start a block), then score every card's `{.exercise}` text against every block of its own section by
tf-idf cosine over alphabetic tokens of length ≥ 4 with a stop list.

Result: **193 of 206 cards score highest against their own printed number**. The 13 that do not were
each read by hand against the print:

| card | why the automated match failed | verdict |
|---|---|---|
| E-SS2.EX-4 | statement is a single displayed formula | matches printed 4 |
| E-SS3.EX-3, EX-4, EX-6, EX-8 | single displayed formulas, neighbours share the vocabulary | match printed 3, 4, 6, 8 |
| E-SS3.EX-7 | printed 7 and 8 are near-identical integrals | matches printed 7 |
| E-SS5.EX-9 | formula only | matches printed 9 |
| E-SS6.EX-1 | formula only (Γ(s) as a limit) | matches printed 1 |
| E-SS6.EX-2 | printed 2's second sentence quotes the sin-product formula, which is printed 3's topic | matches printed 2 |
| E-SS8.PR-1 | printed 1 and 2 are both about angles and conformality | matches printed 1 |
| E-SS9.EX-2 | statement begins "Suppose that a1 , . . . , ar and b1 , . . . , br . . ." | matches printed 2 |
| E-SS9.PR-1 | S1 / S2 / S3 vocabulary shared with printed 2 | matches printed 1 |
| E-SS10.EX-3 | printed 3 opens "More generally, …", which reads like a continuation of 2 | matches printed 3 |

So no card holds a neighbour's statement at the level this test can see. It is a vocabulary test,
not a proof-read: a card that corrects one symbol inside an otherwise matching statement would
still pass.
