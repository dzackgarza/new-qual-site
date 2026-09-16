---
schema: qual/card@1
id: P-TRIV-DE24
kind: problem
title: Frobenius series for the Bessel functions $J_{\pm p}$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Differential Equations, Problem 24, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Removed stray =0 residue against Differential Equations Problem 24 on page 24 of the source PDF and added a remark on the source's undefined n in the normalization.
---

::: problem
Bessel equation of order $p$ is
$$
x^2 y'' + x y' + (x^2 - p^2) y = 0
\tag{36}
$$
Assuming $y = \sum_{m=0} a_m x^{r+m}$, find the two roots of the indicial equation (the two possible values of $r$).
For both of them, solve the recurrence relation for the $a_i$.
You should find, for the largest root, $J_p(x) = \sum_{k=0}^\infty \frac{(-1)^k}{k!\,\Gamma(k+p+1)} \left(\frac{x}{2}\right)^{2k+p}$, and for the smallest $J_{-p}(x) = \sum_{k=0}^\infty \frac{(-1)^k}{k!\,\Gamma(k-p+1)} \left(\frac{x}{2}\right)^{2k-p}$ (for the normalization, assume that $a_0 = \frac{1}{2^n n!}$).
These are Bessel function of the first kind.
:::

::: {.remark}
The normalization $a_0 = \frac{1}{2^n n!}$ in the source uses an undefined $n$.
The stated series have leading coefficient $a_0 = \frac{1}{2^p\,\Gamma(p+1)}$ for $J_p$ and $a_0 = \frac{1}{2^{-p}\,\Gamma(1-p)}$ for $J_{-p}$; the source's formula is the case $p = n \in \mathbb{N}_0$ of the first.
:::
