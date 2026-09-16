---
schema: qual/card@1
id: FT-H6AWV
kind: theorem
title: Fubini--Tonelli theorem
prompts:
- What hypotheses let Fubini-Tonelli exchange the order of integration?
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
Let $f\colon\RR^n\times\RR^k\to\CC$ be [[D-DHFN4|Lebesgue measurable]] on $\RR^{n+k}$, and suppose that one of the iterated integrals of $\abs{f}$ is finite:
$$
\int_{\RR^k}\qty{\int_{\RR^n}\abs{f(x,y)}\,dx}dy<\infty \quad\text{or}\quad \int_{\RR^n}\qty{\int_{\RR^k}\abs{f(x,y)}\,dy}dx<\infty.
$$
Then $f\in L^1(\RR^{n+k})$, and
$$
\int_{\RR^{n+k}} f(x,y)\,d(x,y)=\int_{\RR^k}\qty{\int_{\RR^n} f(x,y)\,dx}dy=\int_{\RR^n}\qty{\int_{\RR^k} f(x,y)\,dy}dx,
$$
where the inner integrals exist for almost every value of the outer variable.
:::

::: {.proof}
By [[FT-4JRQX|Tonelli's theorem]] applied to the nonnegative measurable function $\abs{f}$, $\int_{\RR^{n+k}}\abs{f}$ equals each iterated integral of $\abs{f}$, so it is finite and $f\in L^1(\RR^{n+k})$.
Fubini's theorem for $f\in L^1(\RR^{n+k})$ then gives the equality of $\int_{\RR^{n+k}}f$ with both iterated integrals of $f$.
:::
