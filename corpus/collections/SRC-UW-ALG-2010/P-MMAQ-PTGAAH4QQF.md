---
schema: qual/card@1
id: P-MMAQ-PTGAAH4QQF
kind: problem
title: An algebraic extension of a characteristic-zero field in which every polynomial
  over $F$ has a root is algebraically closed
classification:
  areas:
  - algebra
  topics:
  - Field Extensions
  - Splitting Fields
  - Galois Theory
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-10
---

::: {.problem}
Let $F$ be a field of characteristic zero, and let $K$ be an *algebraic* extension of $F$ that possesses the following property: every polynomial $f\in F[x]$ has a root in $K$.
Show that $K$ is algebraically closed.\\

> **Hint:** if $K(\theta)/K$ is algebraic, consider $F(\theta)/F$ and its normal closure; primitive elements might be of help.
:::


::: {.solution}
<1>1. Let $\theta$ be any element algebraic over $K$. Then $\theta$ is algebraic over $F$.
::: {.proof}
The extension $K/F$ is algebraic by hypothesis, and $\theta/K$ is algebraic. Algebraicity is transitive, so $\theta$ is algebraic over $F$.
:::

<1>2. Let $N/F$ be the normal closure of $F(\theta)/F$. Then $N/F$ is a finite Galois extension.
::: {.proof}
Since $\theta$ is algebraic over $F$, the extension $F(\theta)/F$ is finite. Because $\operatorname{char}F=0$, every algebraic extension of $F$ is separable. Hence the normal closure of the finite separable extension $F(\theta)/F$ is finite, normal, and separable, i.e. finite Galois.
:::

<1>3. There exists $\alpha\in N$ such that
\[
N=F(\alpha).
\]
::: {.proof}
By the primitive element theorem, every finite separable extension is simple. Apply this to the finite Galois extension $N/F$ from <1>2.
:::

<1>4. Let $m_\alpha(x)\in F[x]$ be the minimal polynomial of $\alpha$ over $F$. By hypothesis, $m_\alpha$ has a root $\beta\in K$.
:::

<1>5. In fact $\beta\in N$ and $F(\beta)=N$.
::: {.proof}
Work inside a common algebraic closure containing $K$ and $N$. Since $N/F$ is normal and $\alpha\in N$, the minimal polynomial $m_\alpha$ splits completely over $N$. Therefore every root of $m_\alpha$, in particular $\beta$, lies in $N$.

Because $m_\alpha$ is irreducible over $F$ and $\beta$ is one of its roots,
\[
[F(\beta):F]=\deg m_\alpha=[F(\alpha):F]=[N:F].
\]
But $F(\beta)\subseteq N$, so equality of degrees forces
\[
F(\beta)=N.
\]
:::

<1>6. Therefore $N\subseteq K$, and hence $\theta\in K$.
::: {.proof}
By <1>4, $\beta\in K$, so $F(\beta)\subseteq K$. By <1>5, $F(\beta)=N$, hence $N\subseteq K$. Since $\theta\in F(\theta)\subseteq N$, we get $\theta\in K$.
:::

<1>7. The field $K$ is algebraically closed.
::: {.proof}
We have shown that every element algebraic over $K$ already belongs to $K$. Equivalently, $K$ has no proper algebraic extension. If a nonconstant polynomial in $K[x]$ had no root in $K$, an irreducible factor of degree at least $2$ would have a root in some algebraic extension of $K$, contradicting <1>6. Thus every nonconstant polynomial over $K$ has a root in $K$, so $K$ is algebraically closed.
:::
