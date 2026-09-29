---
schema: qual/card@1
id: P-AGXVARCANONICALPN
kind: problem
title: The canonical bundle of projective space
classification:
  areas:
  - algebraic-geometry
  topics:
  - Canonical Bundle
  - Line Bundles
  - Projective Space
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-20
  note: >-
    Read Exercise 20.3 in the recorded Zaidenberg problem-list PDF. The
    source states K_{P^n} ~ -(n+1)H; the current card's O(n-1) statement was
    a transcription error.
- event: source-corrected
  by: chatgpt
  date: 2026-09-20
  note: >-
    Replaced the false O(n-1) statement by the source's canonical-divisor
    formula K_{P^n} ~ -(n+1)H, equivalently omega_{P^n} ~= O(-n-1).
- event: solution-written
  by: chatgpt
  date: 2026-09-20
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-20
  note: >-
    Checked the Euler sequence, determinant computation, and conversion from
    the canonical line bundle to the canonical divisor class.
---

::: {.problem}
Show that the canonical divisor of $\PP^n$ satisfies
$$
K_{\PP^n}\sim -(n+1)H,
$$
where $H\subseteq\PP^n$ is a hyperplane.
:::

::: {.solution}

::: pf

::: {.pf-step #euler-sequence}
The Euler sequence on $\PP^n$ is
$$
0
\longrightarrow
\OO_{\PP^n}
\longrightarrow
\OO_{\PP^n}(1)^{\oplus(n+1)}
\longrightarrow
T_{\PP^n}
\longrightarrow
0.
$$

::: pf-proof
This is the Euler sequence for projective space [[T-MODEULER]].
:::

:::

::: {.pf-step #determinant-tangent-bundle}
Taking determinants in step [](#euler-sequence){.pf-ref} gives
$$
\boxed{\det T_{\PP^n}\cong\OO_{\PP^n}(n+1)}.
$$

::: pf-proof
For a short exact sequence of locally free sheaves
$$
0\to\mce'\to\mce\to\mce''\to0,
$$
one has
$$
\det\mce\cong\det\mce'\tensor\det\mce''.
$$
Applying this to the Euler sequence yields
$$
\det\bigl(\OO(1)^{\oplus(n+1)}\bigr)
\cong
\det(\OO)\tensor\det(T_{\PP^n}).
$$
The left side is
$$
\OO(1)^{\tensor(n+1)}
\cong
\OO(n+1),
$$
and $\det(\OO)\cong\OO$.
Hence
$$
\det T_{\PP^n}\cong\OO(n+1).
$$
:::

:::

::: {.pf-step #canonical-bundle-op-n-1}
The canonical line bundle is
$$
\boxed{\omega_{\PP^n}\cong\OO_{\PP^n}(-n-1)}.
$$

::: pf-proof
Because $\PP^n$ is smooth of dimension $n$,
$$
\omega_{\PP^n}
=
\det\Omega^1_{\PP^n}
=
\dualof{(\det T_{\PP^n})}.
$$
Step [](#determinant-tangent-bundle){.pf-ref} therefore gives
$$
\omega_{\PP^n}
\cong
\dualof{\OO(n+1)}
\cong
\OO(-n-1).
$$
:::

:::

::: {.pf-step #canonical-divisor-formula}
If $H$ is a hyperplane, then
$$
\boxed{K_{\PP^n}\sim -(n+1)H}.
$$

::: pf-proof
The hyperplane divisor $H$ corresponds to the line bundle
$$
\OO_{\PP^n}(H)\cong\OO_{\PP^n}(1).
$$
Thus
$$
\OO_{\PP^n}\bigl(-(n+1)H\bigr)
\cong
\OO_{\PP^n}(-n-1).
$$
By step [](#canonical-bundle-op-n-1){.pf-ref} this is the canonical line bundle.
Therefore the canonical divisor class is
$$
K_{\PP^n}\sim -(n+1)H.
$$
:::

:::

::: pf-qed
Step [](#canonical-divisor-formula){.pf-ref} is the asserted linear equivalence, and step [](#canonical-bundle-op-n-1){.pf-ref} is its equivalent canonical-bundle form.
:::

:::

:::
