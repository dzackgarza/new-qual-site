# Chapter 9: An Introduction to Elliptic Functions — gap report (SRC-TEXT-SS03)

**Source of truth.** `assets/attachments/Stein-Shakarchi-Complex-Analysis.pdf` (398 pp., OCR'd).
The whole file was extracted with `pdftotext -layout`; the whole-book page map was then taken
from the printed Contents (PDF pp.12-15). Offset: **PDF page = printed page + 19** (checked at
several anchors: printed "4 Exercises 24" -> PDF 43; printed p.32 opens Chapter 2 -> PDF 51;
printed p.318 opens Appendix A -> PDF 337). Quotations below are the OCR as it comes out,
including its mangling of symbols; I say where the OCR is ambiguous.

## 1. Printed inventory of this chapter

| section | heading line | printed pp. | PDF pp. | printed items | starred |
|---|---|---|---|---|---|
| Exercises | `3 Exercises` (p.278) | 278-280 | 297-299 | 1-8 (8 items) | none |
| Problems | `4 Problems` (p.281) | 281-282 | 300-301 | 1-4 (4 items) | 3*, 4* |

## 2. Cards on disk (re-derived from the filesystem, not from the brief)

| directory | files | numbers |
|---|---|---|
| `ch9-exercises/` | 8 | E-SS9.EX-1 .. E-SS9.EX-8 |
| `ch9-problems/` | **3** | E-SS9.PR-1, E-SS9.PR-2, E-SS9.PR-3 |

## 3. Missing items

**One problem has no card: PR-4 (starred).**

### ch9 problem 4 — printed p.282 (PDF p.301), **starred** (`4.∗`)
> Suppose τ is purely imaginary, say τ = it with t > 0. Consider the division of the complex plane
> into congruent rectangles obtained by considering the lines x = n/2, y = tm/2 as n and m range
> over the integers. (An example is the rectangle whose vertices are 0, 1/2, 1/2 + τ /2, and τ /2.)
> (a) Show that ℘ is real-valued on all these lines, and hence on the boundaries of all these
> rectangles.
> (b) Prove that ℘ maps the interior of each rectangle conformally to the upper (or lower)
> half-plane.

Target: `corpus/collections/SRC-TEXT-SS03/ch9-problems/E-SS9.PR-4.md`

(`℘` is the Weierstrass ℘ function; the OCR prints it as a script letter that comes out of
`pdftotext` as `℘` on this page.)

## 4. Statement-fidelity notes (cheap checks only)

Screened all 11 cards for a dropped `[Hint ...]`: none lost.

Note that the existing card PR-2 says in its frontmatter that it was checked "together with
problem 1(b) of the same section" — the section's problem 4 has no card at all, i.e. the
`completion: complete` claim in `index.md` again overstates.

No other statement comparison was made for this chapter.

## 5. Scope of this conclusion

Complete for existence and numbering (12 printed items, 11 cards). Not checked: statement
wording beyond the hint screen; proofs.
