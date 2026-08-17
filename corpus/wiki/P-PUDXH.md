---
schema: qual/card@1
id: P-PUDXH
kind: problem
title: "Let $f, g$ be non-negative measurable functions on $[0, \\infty)$ with"
classification:
  areas:
  - real-analysis
  topics:
  - integrals
  - fubini-tonelli
  - norms
relations: []
review: draft
---

::: problem
Let $f, g$ be non-negative measurable functions on $[0, \infty)$ with
\[
A &\da \int_0^{\infty } f(y) y^{-1/2} \dy < \infty \\
B &\da \qty{ \int_0^{\infty } \abs{ g(y) } }^2 \dy < \infty  
.\]

Show that
\[
\int_0^{\infty } \qty{ \int_0^{\infty } f(y) \dy } {g(x) \over x} \dx \leq AB
.\]
:::

::: {.solution}
> **AI-Generated Solution**

*Setup note.* The statement as printed is garbled: the inner integral $\int_0^\infty f(y)\,dy$ does not depend on $x$ and is typically infinite, and the definition of $B$ is malformed. The natural intended statement (a Hardy-type inequality) is: for non-negative measurable $f, g$ on $[0,\infty)$ with
\[
A \da \int_0^\infty f(y)\, y^{-1/2}\, dy < \infty, \qquad B \da \qty{\int_0^\infty g(y)^2\, dy}^{1/2} < \infty,
\]
one has
\[
\int_0^\infty \frac{g(x)}{x} \int_0^x f(y)\, dy \; dx \le AB.
\]
We prove this corrected form.

<1>1. Write $F(x) \da \int_0^x f(y)\,dy$ and expand the double integral by Tonelli.
    Proof: all integrands are non-negative, so Tonelli applies:
    \[
    \int_0^\infty \frac{g(x)}{x} F(x)\, dx = \int_0^\infty \frac{g(x)}{x} \int_0^x f(y)\,dy\,dx = \int_0^\infty f(y) \int_y^\infty \frac{g(x)}{x}\, dx\, dy .
    \]
<1>2. Bound the inner integral for each fixed $y > 0$.
    Proof: by Cauchy--Schwarz,
    \[
    \int_y^\infty \frac{g(x)}{x}\, dx \le \qty{\int_y^\infty g(x)^2\,dx}^{1/2} \qty{\int_y^\infty x^{-2}\,dx}^{1/2} \le B \cdot y^{-1/2}.
    \]
<1>3. Conclude.
    Proof: substituting <1>2 into <1>1,
    \[
    \int_0^\infty \frac{g(x)}{x} F(x)\,dx \le \int_0^\infty f(y)\, B y^{-1/2}\, dy = BA.
    \]
<1>4. Q.E.D.
:::
