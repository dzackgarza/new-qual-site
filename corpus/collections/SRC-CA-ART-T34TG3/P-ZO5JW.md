---
schema: qual/card@1
id: P-ZO5JW
kind: problem
title: Injective entire functions are of the form $az+b$
classification:
  areas:
  - complex-analysis
  topics:
  - Entire Functions
  - Casorati-Weierstrass
  - Biholomorphisms
  - Singularities
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: {.problem}
Prove that all entire functions that are injective are of the form $f(z) = az + b$ with $a,b\in \CC$ and $a\neq 0$.

> Hint: Apply the Casorati-Weierstrass theorem to $f(1/z)$.
:::

::: {.solution}
Let $f: \CC \to \CC$ be an injective entire function, with Taylor series $f(w)=\sum_{n\ge0}b_nw^n$, and let $g(z) = f(1/z)$ on the punctured disc $\DD^* = \{z \in \CC : 0 < \abs{z} < 1\}$. Then $g(z)=\sum_{n\ge0}b_nz^{-n}$ on $\DD^*$, and $z = 0$ is an isolated singularity of $g$.

<1>1. $z=0$ is not an essential singularity of $g$.

::: {.proof}
Suppose it were. By the Casorati--Weierstrass theorem, $g(\DD^*) = f(\CC \setminus \overline{\DD})$ is dense in $\CC$. Since $f$ is injective, it is nonconstant, so by the open mapping theorem $f(\DD)$ is a nonempty open set. Hence $f(\DD)$ meets $f(\CC \setminus \overline{\DD})$: there are $z_1 \in \DD$ and $z_2 \in \CC \setminus \overline{\DD}$ with $f(z_1) = f(z_2)$. Since $\abs{z_1} < 1 < \abs{z_2}$, $z_1 \neq z_2$, contradicting injectivity.
:::

<1>2. $z=0$ is not a removable singularity of $g$.

::: {.proof}
If it were, $g$ would be bounded near $0$, so $f$ would be bounded on $\abs w>R$ for some $R$, hence bounded on $\CC$. By Liouville's theorem $f$ would be constant, contradicting injectivity.
:::

<1>3. $f$ is a polynomial of degree $m\ge1$.

::: {.proof}
By steps <1>1 and <1>2, $z=0$ is a pole of $g$, of some order $m\ge1$. The Laurent expansion $g(z)=\sum_{n\ge0}b_nz^{-n}$ then has $b_n=0$ for $n>m$ and $b_m\neq0$, so $f(w)=\sum_{n=0}^m b_nw^n$ has degree $m$.
:::

<1>4. $m = 1$.

::: {.proof}
Suppose $m\ge2$. The critical values of $f$ are the finitely many values $f(c)$ with $f'(c)=0$. Choose $c_0\in\CC$ not among them. By the fundamental theorem of algebra, $f(z) = c_0$ has $m$ roots counted with multiplicity, and each is simple because $f'$ does not vanish there. So $f$ takes the value $c_0$ at $m\ge2$ distinct points, contradicting injectivity.
:::

<1>5. Q.E.D.

::: {.proof}
By steps <1>3 and <1>4, $f(z) = \boxed{az + b}$ with $a=b_1\neq0$ and $b=b_0$.
:::
:::
