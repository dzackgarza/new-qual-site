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
Define $e=f\circ g:N\to N$. The given identity $g\circ f=\operatorname{id}_M$ implies $e^2=e$.

<1>1. The endomorphism $e$ is a projection with image $\operatorname{im}f$ and kernel $\ker g$.

::: {.proof}
Since $e=f\circ g$, its image is contained in $\operatorname{im}f$. For $m\in M$, one has $e(f(m))=f(g(f(m)))=f(m)$, proving the reverse inclusion. If $g(n)=0$, then $e(n)=0$. Conversely, if $e(n)=0$, then $g(n)=g(f(g(n)))=g(e(n))=0$. Thus $\ker e=\ker g$.
:::

<1>2. The morphisms
\[
\alpha:\operatorname{im}f\oplus\ker g\longrightarrow N,\qquad (u,v)\longmapsto u+v,
\]
and
\[
\beta:N\longrightarrow\operatorname{im}f\oplus\ker g,\qquad n\longmapsto(e(n),n-e(n))
\]
are well-defined $R$-linear morphisms.

::: {.proof}
By step <1>1, $e(n)\in\operatorname{im}f$. Moreover, $g(n-e(n))=g(n)-g(f(g(n)))=0$, so $n-e(n)\in\ker g$. Both maps are $R$-linear because $e$ and the module operations are $R$-linear.
:::

<1>3. The required decomposition is
\[
\boxed{N\cong\operatorname{im}f\oplus\ker g}.
\]

::: {.proof}
For every $n\in N$, $\alpha\beta(n)=e(n)+n-e(n)=n$. For $u\in\operatorname{im}f$ and $v\in\ker g$, step <1>1 gives $e(u)=u$ and $e(v)=0$, whence $\beta\alpha(u,v)=(u,v)$. Thus $\alpha$ and $\beta$ are inverse $R$-module isomorphisms.
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 proves the claimed direct-sum decomposition.
:::
:::

