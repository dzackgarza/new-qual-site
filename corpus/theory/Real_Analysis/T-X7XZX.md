---
schema: qual/card@1
id: T-X7XZX
kind: theorem
title: Fubini--Tonelli theorem
prompts:
- What hypotheses let Fubini-Tonelli exchange the order of integration?
slogan: 'On a product of $\sigma$-finite spaces, if one iterated integral of $\abs{f}$ is finite, then $f\in L^1$ and both iterated integrals of $f$ equal $\int f$.'
classification:
  areas:
  - real-analysis
  topics:
  - Fubini-Tonelli
  - Integrals
relations: []
review: draft
---

::: {.theorem}
Let $(X,\mcm,\mu)$ and $(Y,\mcn,\nu)$ be $\sigma$-finite [[D-QYLPH|measure]] spaces, and let $f\colon X\times Y\to\CC$ be $\mcm\otimes\mcn$-[[D-DHFN4|measurable]]. Suppose that one of the iterated integrals of $\abs{f}$ is finite:
$$
\int_X\qty{\int_Y\abs{f(x,y)}\,d\nu(y)}d\mu(x)<\infty\quad\text{or}\quad\int_Y\qty{\int_X\abs{f(x,y)}\,d\mu(x)}d\nu(y)<\infty.
$$
Then $f\in L^1(X\times Y,\mu\times\nu)$, and
$$
\int_{X\times Y}f\,d(\mu\times\nu)=\int_X\qty{\int_Y f(x,y)\,d\nu(y)}d\mu(x)=\int_Y\qty{\int_X f(x,y)\,d\mu(x)}d\nu(y),
$$
where the inner integrals exist for almost every value of the outer variable.
:::

::: {.remark title="Variations"}
For Lebesgue measure on $\RR^{n+k}=\RR^n\times\RR^k$ the theorem holds for every [[D-DHFN4|Lebesgue measurable]] $f\colon\RR^{n+k}\to\CC$, not only for $f$ measurable for the product of the Lebesgue $\sigma$-algebras: if one iterated integral of $\abs{f}$ is finite, then $f\in L^1(\RR^{n+k})$ and
$$
\int_{\RR^{n+k}} f(x,y)\,d(x,y)=\int_{\RR^k}\qty{\int_{\RR^n} f(x,y)\,dx}dy=\int_{\RR^n}\qty{\int_{\RR^k} f(x,y)\,dy}dx .
$$
The proof uses the forms of [[FT-4JRQX|Tonelli's theorem]] and Fubini's theorem for the completed product measure: Tonelli's theorem applied to $\abs{f}$ shows that $\int_{\RR^{n+k}}\abs{f}$ equals each iterated integral of $\abs{f}$, so $f\in L^1(\RR^{n+k})$, and Fubini's theorem for $f$ then gives the equalities.
:::
