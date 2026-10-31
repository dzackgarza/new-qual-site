---
schema: qual/card@1
id: P-UWALG07-4
kind: problem
title: $\ZZ[i]$ is a UFD; is $\ZZ[\sqrt{-5}]$?
classification:
  areas:
  - algebra
  topics:
  - Rings
  - Unique Factorization Domains
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-10-31
---

::: {.problem}
(a) Show that the ring $\ZZ[i]$ of Gaussian integers is a unique factorisation domain (UFD).

(b) Is $\ZZ[\sqrt{-5}]$ a UFD?
Justify your answer.
:::

::: {.solution}
For $z=a+bi\in\ZZ[i]$ put $N(z)=a^2+b^2$, and for $w=a+b\sqrt{-5}\in\ZZ[\sqrt{-5}]$ put $N(w)=a^2+5b^2$; in both rings $N$ is multiplicative and $N(u)=1$ exactly for the units, which are $\pm1$ in both rings.

::: pf

::: {.pf-step #part-a}
(a) $\ZZ[i]$ is a unique factorization domain.

::: pf-proof
It is enough to show that $N$ is a Euclidean function on $\ZZ[i]$, since a Euclidean domain is a unique factorization domain.
Let $z,w\in\ZZ[i]$ with $w\ne0$. In $\QQ(i)$ the quotient $z/w=z\overline w/N(w)$ has rational real and imaginary parts; choose integers $m,n$ with $\abs{\operatorname{Re}(z/w)-m}\le\frac12$ and $\abs{\operatorname{Im}(z/w)-n}\le\frac12$ and set $q=m+ni\in\ZZ[i]$.
Then
$$
N(z/w-q)=\Bigl(\operatorname{Re}(z/w)-m\Bigr)^2+\Bigl(\operatorname{Im}(z/w)-n\Bigr)^2\le\frac12<1,
$$
so $N(z-qw)=N(w)N(z/w-q)<N(w)$.
Hence $\ZZ[i]$ is Euclidean, in particular a unique factorization domain.
:::

:::

::: {.pf-step #part-b}
(b) $\ZZ[\sqrt{-5}]$ is not a unique factorization domain.

::: pf-proof
The four elements $2$, $3$, $1+\sqrt{-5}$ and $1-\sqrt{-5}$ are irreducible.
Indeed $N(2)=4$, $N(3)=9$ and $N(1\pm\sqrt{-5})=6$, so a nontrivial factorization of $2$ would need an element of norm $2$, one of $3$ would need an element of norm $3$, and one of $1\pm\sqrt{-5}$ would need an element of norm $2$ or $3$; but $a^2+5b^2\in\{2,3\}$ has no integer solution, since $b=0$ forces $a^2\in\{2,3\}$.
Moreover
$$
6=2\cdot3=(1+\sqrt{-5})(1-\sqrt{-5}),
$$
and these are two factorizations into irreducibles that are not related by units: all four factors are pairwise non-associate, because associates have equal norm and $N(2)=4$, $N(3)=9$, $N(1\pm\sqrt{-5})=6$ are pairwise distinct.
Hence $\ZZ[\sqrt{-5}]$ is not a unique factorization domain.
:::

:::

:::

:::
