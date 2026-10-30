---
schema: qual/card@1
id: P-DURCM
kind: problem
title: $N\cong\im f\oplus\ker g$ when $g\circ f=\id_M$
classification:
  areas:
  - algebra
  topics:
  - Exact Sequences
  - Modules
  - Projective Modules
relations: []
review: draft
---

::: {.problem}
Let $R$ be a ring and $f: M\to N$ and $g: N\to M$ be $R\dash$module homomorphisms such that $g\circ f = \id_M$.
Show that $N \cong \im f \oplus \ker g$.
:::

::: {.solution}

::: pf

::: {.pf-step #sum}

$N=\im f+\ker g$.

::: pf-proof

For $n\in N$ write $n=\bigl(n-f(g(n))\bigr)+f(g(n))$. The second term lies in $\im f$. The first lies in $\ker g$, because
$$
g\bigl(n-f(g(n))\bigr)=g(n)-(g\circ f)(g(n))=g(n)-g(n)=0.
$$

:::

:::

::: {.pf-step #direct}

$\im f\cap\ker g=0$.

::: pf-proof

If $n=f(m)$ and $g(n)=0$, then $m=(g\circ f)(m)=g(n)=0$, so $n=f(0)=0$.

:::

:::

::: pf-qed

By Steps [](#sum){.pf-ref} and [](#direct){.pf-ref}, the addition map $\im f\oplus\ker g\to N$, $(a,b)\mapsto a+b$, is a surjective and injective $R$-module homomorphism. Hence
$$
\boxed{N\cong\im f\oplus\ker g.}
$$

:::

:::

:::
