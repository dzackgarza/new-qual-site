---
schema: qual/card@1
id: P-GRECH2-11
kind: problem
title: Limit of $(f(x+3h^2)-f(x-h^2))/(2h^2)$
classification:
  areas: [prelim]
  topics:
  - Differentiation
  - Limits
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Checked against Question 11 of the Chapter 2 review questions in assets/attachments/extracted/chapter-2.md (Mistral OCR), compared with the same page in the Cracking the GRE Mathematics Subject Test book extraction.
---

::: {.problem}
If $f(x)$ is a function that's differentiable everywhere, what is the value of this limit?

$$
\lim_{h \to 0} \frac{f(x + 3h^2) - f(x - h^2)}{2h^2}
$$

(A) $4f'(x)$
(B) $2f'(x)$
(C) $f'(x)$
(D) $\frac{1}{2}f'(x)$
(E) The limit does not exist.
:::

::: {.solution}

Because $f$ is differentiable at $x$, write
$$
f(x+u)=f(x)+f'(x)u+r(u),
\qquad
\frac{r(u)}{u}\longrightarrow0
$$
as $u\to0$.

::: pf

::: {.pf-step #s1-1}

The numerator satisfies
$$
f(x+3h^2)-f(x-h^2)
=4f'(x)h^2+o(h^2).
$$


::: pf-proof

Apply the differentiability expansion with $u=3h^2$ and $u=-h^2$:
$$
f(x+3h^2)
=f(x)+3f'(x)h^2+r(3h^2),
$$
$$
f(x-h^2)
=f(x)-f'(x)h^2+r(-h^2).
$$
Subtracting gives
$$
4f'(x)h^2+r(3h^2)-r(-h^2).
$$
Since $r(u)=o(u)$, both $r(3h^2)$ and $r(-h^2)$ are $o(h^2)$, proving the claim.

:::

:::

::: {.pf-step #s1-2}

The limit is
$$
\boxed{2f'(x)},
$$
so the answer is (B).


::: pf-proof

Divide the relation in step [](#s1-1){.pf-ref} by $2h^2$ for $h\ne0$:
$$
\frac{f(x+3h^2)-f(x-h^2)}{2h^2}
=2f'(x)+o(1).
$$
Taking $h\to0$ gives the displayed limit.

:::

:::

::: pf-qed

Step [](#s1-2){.pf-ref} gives the requested value using only the stated differentiability hypothesis.

:::

:::

:::
