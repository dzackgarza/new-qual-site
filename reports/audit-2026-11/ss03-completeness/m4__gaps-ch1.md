# SRC-TEXT-SS03 — Chapter 1 (Preliminaries to Complex Analysis)

**No missing cards.** Chapter 1 prints only an Exercise block (§4, "4 Exercises", PDF pages
43–50; PDF page 51 opens chapter 2) and **no Problem section**. Printed count 26, cards
present 26 (`E-SS1.EX-1` … `E-SS1.EX-26`), numbering verified contiguous in the print.
PDF page = printed folio + 19 (PDF 43 = printed 24, PDF 50 = printed 31).

Scope of the fidelity claim below: **all 26 cards**, statement blocks read against the
printed items. No proof was audited.

## Statement fidelity — 4 printed hints dropped (undocumented), 2 statement changes (1 documented)

In each of the four hint cases below the card has no `::: {.hint}` block, no `remark`
mentioning a hint, and its `audit:` list holds only bare `source-checked` /
`solution-written` / `solution-reviewed` events with no note — so the loss is not recorded
anywhere on the card. (By contrast, the chapter 6 and chapter 10 cards do record their
statement repairs; see `gaps-ch6.md`.)

### `E-SS1.EX-15` (PDF p. 47) — bracketed hint and a printed sentence dropped
Print, after the displayed limit (OCR verbatim):

> [Hint: Sum by parts.] In other words, if a series converges, then it is Abel summable
> with the same limit. For the precise definition of these terms, and more information
> on summability methods, we refer the reader to Book I, Chapter 2.

Card: keeps only "In other words, a convergent series is Abel summable to its ordinary
sum." — the `[Hint: Sum by parts.]` is gone and the Book I cross-reference sentence is gone.
(The hint's content is used inside the card's solution, which cites the summation-by-parts
formula of `E-SS1.EX-14`, so nothing mathematical is lost, but the printed bracket is not
reproduced.)

### `E-SS1.EX-16` (PDF p. 47) — bracketed hint dropped, and nowhere in the card
Print, in part (d) (`a_n = (n!)^3/(3n)!`):

> [Hint: Use Stirling’s formula, which says that
>                 1
>      n! ∼ cnn+ 2 e−n for some c > 0..]

Card: part (d) is stated bare. `grep -i stirling` over the whole card file returns nothing,
so the printed hint is lost outright, not merely relocated. The OCR double period `0..]` is
in the print.

### `E-SS1.EX-18` (PDF p. 48) — bracketed hint dropped
Print: "Let f be a power series centered at the origin. Prove that f has a power series
expansion around any point in its disc of convergence. **[Hint: Write z = z0 + (z − z0 )
and use the binomial expansion for z n .]**"
Card: statement only; the binomial expansion is used in the solution but the bracket is not
reproduced anywhere in the card.

### `E-SS1.EX-21` (PDF p. 48) — bracketed hint dropped
Print, after "Justify any change in the order of summation.":

> [Hint: Use the dyadic expansion of an integer and the fact that 2k+1 − 1 = 1 +
> 2 + 22 + · · · + 2k .]

Card: statement ends at "Justify any change in the order of summation."; the word "dyadic"
survives only in the card's `title:` field. The hint itself is not reproduced.

### `E-SS1.EX-13` (PDF p. 47) — hypothesis strengthened (recorded on the card)
Print: "Suppose that f is holomorphic in an **open set** Ω. Prove that in any one of the
following cases: (a) Re(f ) is constant; (b) Im(f ) is constant; (c) |f | is constant; one
can conclude that f is constant."
Card: "Suppose f is holomorphic in a **region Ω (an open connected set)**. If any of the
following hold, then f is constant: …"
The printed hypothesis is an arbitrary open set; the card requires connectedness (which the
conclusion needs — on a disconnected open set f can be constant on each component with
different constants). This one **is** recorded: the audit note reads "Stein-Shakarchi 1.13
says open set; the statement now names the domain, and takes it connected, since constancy
fails on a disconnected open set", and a `remark` says the same. No action needed; listed so
the difference from the print is on the record.

### `E-SS1.EX-11` (PDF p. 46) — cross-reference replaced by content (not recorded)
Print: "**Use Exercise 10** to prove that if f is holomorphic in the open set Ω, then the
real and imaginary parts of f are harmonic; that is, their Laplacian is zero."
Card: "**Use the Wirtinger-operator identity for the Laplacian** to prove …"
Content-equivalent (Exercise 10 is the identity `4∂∂̄ = 4∂̄∂ = Δ`), but the printed pointer is
not preserved and nothing in the card records the substitution — its only `remark` concerns
a different variation ("The statement is often posed without the Wirtinger hint").

## Checked and faithful (no action)

EX-1 … EX-10, EX-12, EX-14, EX-17, EX-19, EX-20, EX-22 … EX-26 reproduce the printed
statement, all sub-parts, all bracketed hints (EX-4, EX-6, EX-7 — two hints, EX-19, EX-22)
and the correct signs/exponents. Two places where the OCR is broken and the card's reading
should be trusted over the OCR, not reported as a card defect:
* `E-SS1.EX-8` and `E-SS1.EX-10`: every overline is lost by the OCR (`∂h/∂z`, `∂f/∂z`), so
  the print reads as nonsense twice; the cards restore `∂h/∂z = (∂g/∂z)(∂f/∂z) +
  (∂g/∂z̄)(∂f/∂z̄)` and `4∂_z∂_z̄ = 4∂_z̄∂_z = Δ`, which are correct.
* `E-SS1.EX-14`: the OCR displaces the whole first line ("Suppose {an }n=1 N and {bn }n=1 N
  are two finite sequences") to the foot of page 47, so the printed item appears to start
  mid-sentence. The card reconstructs it correctly.
* `E-SS1.EX-7`: the print's hypothesis `z̄w ≠ 1` has its bar dropped by OCR and appears as
  `zw = 1`; the card has `\overline{z}w \neq 1`. Correct.
