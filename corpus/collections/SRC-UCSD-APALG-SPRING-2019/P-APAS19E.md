---
schema: qual/card@1
id: P-APAS19E
kind: problem
title: Same character need not imply isomorphic representations of $\mathrm{GL}_2(\RR)$
classification:
  areas:
  - applied-algebra
  topics:
  - Representation Theory
  - Character Theory
relations: []
review: draft
---

::: {.problem}
Let $G=\mathrm{GL}_2(\RR)$ be the group of invertible $2\times 2$ real matrices and let $X,Y\colon G\to\mathrm{GL}_d(\CC)$ be two complex matrix representations of $G$ with the same degree $d$.
If $X$ and $Y$ have the same character, are $X$ and $Y$ necessarily isomorphic?
Justify your answer.
:::

::: {.solution}

No retained solution set covers this exercise: the card's own counterexample follows, with the two representations checked, their characters computed and their non-isomorphism as separate steps.

::: pf

::: {.pf-step #homomorphism}
$\ell(g)=\log\abs{\det g}$ is a homomorphism $\GL_{2}(\RR)\to(\RR,+)$, and $X(g)=\begin{pmatrix}1&\ell(g)\\0&1\end{pmatrix}$ is a representation of degree $2$.

::: pf-proof
$\det(gh)=\det g\det h$, so $\abs{\det(gh)}=\abs{\det g}\abs{\det h}$ and $\ell$ is additive; $\det g\ne0$ for $g$ invertible, so $\ell$ is defined. Then $X(g)X(h)=\begin{pmatrix}1&\ell(g)\\0&1\end{pmatrix}\begin{pmatrix}1&\ell(h)\\0&1\end{pmatrix}=\begin{pmatrix}1&\ell(g)+\ell(h)\\0&1\end{pmatrix}=X(gh)$, and $X(e)=I_{2}$, so $X$ is a representation of degree $2$.
:::

:::

::: {.pf-step #characters}
$X$ and $Y(g)=I_{2}$ have the same character: $\operatorname{tr}X(g)=2=\operatorname{tr}Y(g)$ for every $g$.

::: pf-proof
The trace of $\begin{pmatrix}1&\ell(g)\\0&1\end{pmatrix}$ is $1+1=2$, and the trace of $I_{2}$ is $2$.
:::

:::

::: {.pf-step #not-iso}
$X$ and $Y$ are not isomorphic.

::: pf-proof
An isomorphism of representations intertwining $X$ with the trivial representation $Y$ would force $X(g)v=v$ for every $g$ and every $v$ in the underlying space, that is $X(g)=I_{2}$ for all $g$. But $\ell(g)\ne0$ for instance for $g=2I_{2}$, where $\ell=\log4\ne0$, so $X(2I_{2})\ne I_{2}$.
:::

:::

::: {.pf-qed}
Two complex representations of $\GL_{2}(\RR)$ of the same finite degree, with equal characters by step [](#characters){.pf-ref}, need not be isomorphic by step [](#not-iso){.pf-ref}; so the answer is no. Character theory loses no information only under hypotheses such as compactness (or finite-dimensionality of the group, i.e. finiteness), which $\GL_{2}(\RR)$ does not satisfy.
:::

:::

:::
