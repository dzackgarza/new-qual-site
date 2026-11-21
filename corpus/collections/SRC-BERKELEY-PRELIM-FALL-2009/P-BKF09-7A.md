---
schema: qual/card@1
id: P-BKF09-7A
kind: problem
title: The Schwarzian derivative is holomorphic at a simple pole
classification:
  areas:
  - prelim
  topics:
  - Complex Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Moved the displayed expression and all TeX in the statement and solution inside math delimiters against f09solutions.pdf page 3 problem 7A.
---

::: {.problem}
If $f$ is a meromorphic function which has a pole of order 1 at $z_0$ show that

$$
\frac{f'''(z)}{f'(z)} - \frac{3}{2} \left( \frac{f''(z)}{f'(z)} \right)^2
$$

can be extended to a holomorphic function at $z_0$.
:::

::: {.solution}

The argument is the card's own: a simple pole contributes the singular part of a Möbius map, whose Schwarzian derivative vanishes, so the displayed expression is holomorphic.

::: pf

::: {.pf-step #laurent}

Near $z_{0}$, writing $t=z-z_{0}$, $f(t)=at^{-1}+h(t)$ with $a\ne0$ and $h$ holomorphic at $0$; hence $f'=-at^{-2}+h'$, $f''=2at^{-3}+h''$, $f'''=-6at^{-4}+h'''$.

::: pf-proof

A pole of order $1$ with residue $a\ne0$ means exactly that $f(z)-\frac{a}{z-z_{0}}$ has a removable singularity at $z_{0}$, that is, equals a holomorphic $h(z)$ there; in the variable $t=z-z_{0}$ this is $f=at^{-1}+h(t)$. Differentiating term by term in the punctured disc gives the three displayed identities, $a$ being constant and $h$ holomorphic.

:::

:::

::: {.pf-step #ratios}

$f'''/f'=6t^{-2}+O(1)$ and $f''/f'=-2t^{-1}+O(1)$, so $(f''/f')^{2}=4t^{-2}+O(1)$.

::: pf-proof

Factor out the leading terms: $f'=-at^{-2}\bigl(1+O(t^{2})\bigr)$, since $h'=O(1)$ and $h'(0)$ is absorbed in the $O(t^{2})$ factor after multiplying by $t^{2}$. Then
$$
\frac{f'''}{f'}=\frac{-6at^{-4}\bigl(1+O(t^{4})\bigr)}{-at^{-2}\bigl(1+O(t^{2})\bigr)}=6t^{-2}\bigl(1+O(t^{2})\bigr)=6t^{-2}+O(1),
$$
and similarly $\frac{f''}{f'}=\frac{2at^{-3}(1+O(t^{3}))}{-at^{-2}(1+O(t^{2}))}=-2t^{-1}(1+O(t))$ after expanding $\frac{1+O(t^{3})}{1+O(t^{2})}=1+O(t^{2})$ and multiplying out; squaring gives $4t^{-2}+O(1)$.

:::

:::

::: {.pf-step #holomorphic}

$\displaystyle\frac{f'''}{f'}-\frac32\Bigl(\frac{f''}{f'}\Bigr)^{2}$ is holomorphic at $z_{0}$.

::: pf-proof

By step [](#ratios){.pf-ref} the expression is
$$
\Bigl(6t^{-2}+O(1)\Bigr)-\frac32\Bigl(4t^{-2}+O(1)\Bigr)=6t^{-2}-6t^{-2}+O(1)=O(1)
$$
as $t\to0$, so it is bounded in a punctured neighbourhood of $z_{0}$; a bounded holomorphic function on a punctured disc has a removable singularity, and the extension is holomorphic there:
$$
\boxed{\frac{f'''}{f'}-\frac32\Bigl(\frac{f''}{f'}\Bigr)^{2}\ \text{extends holomorphically across } z_{0}.}
$$

:::

:::

:::

:::
