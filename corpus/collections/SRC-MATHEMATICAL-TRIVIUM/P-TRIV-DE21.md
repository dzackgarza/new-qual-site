---
schema: qual/card@1
id: P-TRIV-DE21
kind: problem
title: Perturbative ground-state energy of the quartic anharmonic oscillator
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Differential Equations, Problem 21, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Removed extraction residue in the statement of Differential Equations Problem 21 against pages 23-24 of the source PDF.
---

::: {.problem}
Consider Schrodinger equation for a quantum harmonic oscillator with small quartic perturbation
$$
\left(-\frac{1}{2}\frac{d^2}{dx^2} + \frac{x^2}{2} + \frac{g x^4}{4}\right)\psi(x) = E_0(g)\psi(x)
\tag{30}
$$
and make the ansatz
$$
\psi(x) = e^{-x^2/2} \sum_{n=0}^\infty \left(\frac{g}{4}\right)^n B_n(x) \qquad \text{with} \quad B_0(x) = 1
\tag{31}
$$
$$
E_0(g) = \sum_{k=0}^\infty a_k \left(\frac{g}{4}\right)^k.
\tag{32}
$$
We already know that $a_0 = \frac{1}{2}$ from the unperturbed oscillator.
We want to find the first two corrections $a_1$ and $a_2$.

(a) Find a recurrence relation for $B_k(x)$ and $a_k$

(b) Solve the relation by assuming $B_i(x) = \sum_{j=1}^{2i} x^{2j} (-1)^i B_{i,j}$.

(c) Considering different powers of $x$, find the following relations
$$
a_n = (-1)^{n+1} B_{n,1}
\tag{33}
$$
$$
2j B_{n,j} = (j+1)(2j+1) B_{n,j+1} + B_{n-1,j-2} - \sum_{k=1}^{n-1} B_{n-k,1} B_{k,j}
\tag{34}
$$

(d) Find $a_1$ and $a_2$.
You can check that your result agrees with the usual perturbation theory.
:::
