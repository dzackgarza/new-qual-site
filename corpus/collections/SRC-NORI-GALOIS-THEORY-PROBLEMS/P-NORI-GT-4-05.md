---
schema: qual/card@1
id: P-NORI-GT-4-05
kind: problem
title: $E(X_1,\dots,X_d)/F(X_1,\dots,X_d)$ has the same degree as $E/F$
classification:
  areas: [algebra]
  topics:
  - Rational Function Fields
  - Degree of Field Extensions
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against problem 4.5 of the retained Nori Galois Theory Problems PDF.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Stated the hypothesis on E and F from Problem 4.4, on which this problem depends, from p. 3 of the Nori Galois Theory Problems PDF.
---

::: {.problem}
Let $E$ be a field extension of $F$ of degree $n$.
Show that $E(X_1, \ldots, X_d)$ is a field extension of $F(X_1, \ldots, X_d)$ of degree $n$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The assertion holds for $d=1$.


::: pf-proof

This is exactly Problem 4.4(iii): if $[E:F]=n$, then
$$
[E(X_1):F(X_1)]=n.
$$

:::

:::

::: {.pf-step #s1-2}

Assume for some $d\ge2$ that
$$
[E(X_1,\ldots,X_{d-1}):F(X_1,\ldots,X_{d-1})]=n.
$$
Set
$$
E_{d-1}=E(X_1,\ldots,X_{d-1}),
\qquad
F_{d-1}=F(X_1,\ldots,X_{d-1}).
$$


::: pf-proof

This is the induction hypothesis together with notation for the intermediate fields.

:::

:::

::: {.pf-step #s1-3}

Applying Problem 4.4 to the finite extension
$$
E_{d-1}/F_{d-1}
$$
and the new indeterminate $X_d$ gives
$$
[E_{d-1}(X_d):F_{d-1}(X_d)]=n.
$$


::: pf-proof

By step [](#s1-2){.pf-ref}, the extension $E_{d-1}/F_{d-1}$ has degree $n$. Problem 4.4 states that adjoining one transcendental indeterminate to both fields preserves the degree of a finite extension. Therefore the displayed equality follows.

:::

:::

::: {.pf-step #s1-4}

One has
$$
E_{d-1}(X_d)=E(X_1,\ldots,X_d)
$$
and
$$
F_{d-1}(X_d)=F(X_1,\ldots,X_d).
$$


::: pf-proof

Both equalities are immediate from the definitions of the rational function fields and of $E_{d-1},F_{d-1}$.

:::

:::

::: {.pf-step #s1-5}

Hence
$$
[E(X_1,\ldots,X_d):F(X_1,\ldots,X_d)]=n.
$$


::: pf-proof

Substitute the identifications from step [](#s1-4){.pf-ref} into the degree equality of step [](#s1-3){.pf-ref}.

:::

:::

::: {.pf-step #s1-6}

Therefore, for every $d\ge1$,
$$
\boxed{
[E(X_1,\ldots,X_d):F(X_1,\ldots,X_d)]
=[E:F]
=n.
}
$$


::: pf-proof

Step [](#s1-1){.pf-ref} is the base case, and steps [](#s1-2){.pf-ref} through [](#s1-5){.pf-ref} establish the induction step.

:::

:::

::: pf-qed

Step [](#s1-6){.pf-ref} is the required statement.

:::

:::

:::
