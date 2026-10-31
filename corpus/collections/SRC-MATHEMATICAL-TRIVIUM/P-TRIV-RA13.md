---
schema: qual/card@1
id: P-TRIV-RA13
kind: problem
title: Limit as $x\to0$ involving $\sin\tan x-\tan\sin x$ and $\arcsin\arctan x-\arctan\arcsin x$
classification:
  areas: [real-analysis]
  topics:
  - Limits
  - Taylor Series
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Real Analysis, Problem 13, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md. The exact formula is intentionally left as an extraction gap rather than reconstructed from model inference.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Replaced the unresolved-extraction note with the limit displayed in Real Analysis Problem 13 on page 9 of the source PDF.
---

::: {.problem}
Find $\displaystyle\lim_{x \to 0} \frac{\sin\tan x - \tan\sin x}{\arcsin\arctan x - \arctan\arcsin x}$.
:::

::: {.solution}

::: pf

::: pf-step

The relevant Taylor expansions at $0$ are
$$
\tan x
=
x+\frac{x^3}{3}+\frac{2x^5}{15}+\frac{17x^7}{315}+O(x^9),
$$
$$
\sin x
=
x-\frac{x^3}{6}+\frac{x^5}{120}-\frac{x^7}{5040}+O(x^9),
$$
$$
\arcsin x
=
x+\frac{x^3}{6}+\frac{3x^5}{40}+\frac{5x^7}{112}+O(x^9),
$$
and
$$
\arctan x
=
x-\frac{x^3}{3}+\frac{x^5}{5}-\frac{x^7}{7}+O(x^9).
$$


::: pf-proof

These are the standard Maclaurin expansions through degree $7$.

:::

:::

::: {.pf-step #s1-2}

Composing the first two series gives
$$
\sin(\tan x)
=
x+\frac{x^3}{6}-\frac{x^5}{40}-\frac{55x^7}{1008}+O(x^9),
$$
and
$$
\tan(\sin x)
=
x+\frac{x^3}{6}-\frac{x^5}{40}-\frac{107x^7}{5040}+O(x^9).
$$


::: pf-proof

Substitute the series for $\tan x$ into the sine series and retain terms of
degree at most $7$. Repeat with the sine series substituted into the tangent
series. All omitted terms contribute $O(x^9)$ because the functions are odd.

:::

:::

::: {.pf-step #s1-3}

Therefore
$$
\sin(\tan x)-\tan(\sin x)
=
-\frac{x^7}{30}+O(x^9).
$$


::: pf-proof

Subtract the two expressions in step [](#s1-2){.pf-ref}. The terms of degrees $1$, $3$, and
$5$ cancel, while
$$
-\frac{55}{1008}
+
\frac{107}{5040}
=
-\frac{275-107}{5040}
=
-\frac{168}{5040}
=
-\frac1{30}.
$$

:::

:::

::: {.pf-step #s1-4}

Composing the inverse-function series gives
$$
\arcsin(\arctan x)
=
x-\frac{x^3}{6}+\frac{13x^5}{120}-\frac{341x^7}{5040}+O(x^9),
$$
and
$$
\arctan(\arcsin x)
=
x-\frac{x^3}{6}+\frac{13x^5}{120}-\frac{173x^7}{5040}+O(x^9).
$$


::: pf-proof

Substitute the series for $\arctan x$ into the series for $\arcsin x$, and
then substitute the series for $\arcsin x$ into the series for $\arctan x$,
again retaining terms through degree $7$.

:::

:::

::: {.pf-step #s1-5}

Therefore
$$
\arcsin(\arctan x)-\arctan(\arcsin x)
=
-\frac{x^7}{30}+O(x^9).
$$


::: pf-proof

Subtract the expansions in step [](#s1-4){.pf-ref}:
$$
-\frac{341}{5040}
+
\frac{173}{5040}
=
-\frac{168}{5040}
=
-\frac1{30}.
$$

:::

:::

::: {.pf-step #s1-6}

Hence
$$
\boxed{
\lim_{x\to0}
\frac{\sin\tan x-\tan\sin x}
{\arcsin\arctan x-\arctan\arcsin x}
=1.
}
$$


::: pf-proof

By steps [](#s1-3){.pf-ref} and [](#s1-5){.pf-ref},
$$
\frac{-x^7/30+O(x^9)}{-x^7/30+O(x^9)}
=
\frac{-1/30+O(x^2)}{-1/30+O(x^2)}
\longrightarrow1.
$$

:::

:::

::: pf-qed

Step [](#s1-6){.pf-ref} is the required limit.

:::

:::

:::
