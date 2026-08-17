---
schema: qual/card@1
id: P-HKZVN
kind: problem
title: "Fix a measurable function $f : \\mathbb{R}^2 \\to \\mathbb{R}$ and, for e…"
classification:
  areas:
  - real-analysis
  topics:
  - fubini-tonelli
  - counterexamples
  - integrals
relations: []
review: draft
---

::: {.problem title="?"}
Fix a measurable function $f : \mathbb{R}^2 \to \mathbb{R}$ and, for every $x, y \in \mathbb{R}$, let $$f_x : \mathbb{R} \to \mathbb{R} \text{ and } f_y : \mathbb{R} \to \mathbb{R}$$ be given by $f_x(z) = f(x,z)$ and $f_y(z) = f(z,y)$.
Show that there exists such an $f$ so that $f_x \in L^1(\mathbb{R})$ for a.e. $x$ and $f_y \in L^1(\mathbb{R})$ for a.e. $y$ but $$\int_{\mathbb{R}}\left(\int_{\mathbb{R}} f_x(y)dy\right)dx \ne \int_{\mathbb{R}}\left(\int_{\mathbb{R}} f_y(x)dx\right)dy.$$

What does Fubini's theorem imply about such $f$?
What about Tonelli's theorem?
:::

:::: {.solution}
> **AI-Generated Solution**

<1>1. Construct the function $f$.
    Proof: on the square $(0,1)\times(0,1)$ set $f(x,y) = \dfrac{x^2 - y^2}{(x^2+y^2)^2}$, and set $f = 0$ off the square.
<1>2. For every $x > 0$, $f_x \in L^1(\mathbb{R})$, and for every $y > 0$, $f_y \in L^1(\mathbb{R})$.
    Proof: fixing $x > 0$, the map $y \mapsto f(x,y)$ is continuous on $(0,1]$ and bounded near $y = 0$ (as $x^2 + y^2 \ge x^2 > 0$), so it is integrable on $(0,1)$; it vanishes off $(0,1)$. The argument for $f_y$ is symmetric.
<1>3. The iterated integrals exist but differ.
    Proof: since $\frac{\partial}{\partial y}\left[\frac{y}{x^2+y^2}\right] = \frac{x^2-y^2}{(x^2+y^2)^2}$, integration in $y$ gives
    \[\int_0^1 f(x,y)\,dy = \left[\frac{y}{x^2+y^2}\right]_{y=0}^{1} = \frac{1}{x^2+1},\]
    so $\int_0^1\left(\int_0^1 f(x,y)\,dy\right)dx = \int_0^1 \frac{dx}{1+x^2} = \frac{\pi}{4}$. Similarly $\frac{\partial}{\partial x}\left[\frac{x}{x^2+y^2}\right] = \frac{y^2-x^2}{(x^2+y^2)^2}$ gives $\int_0^1 f(x,y)\,dx = -\frac{1}{1+y^2}$ and hence $\int_0^1\left(\int_0^1 f(x,y)\,dx\right)dy = -\frac{\pi}{4}$. The two iterated integrals, $+\pi/4$ and $-\pi/4$, are unequal.
<1>4. What Fubini's theorem implies about such $f$.
    Proof: Fubini's theorem asserts the equality of the iterated integrals when $f$ is jointly integrable, i.e. $\iint |f| < \infty$. Therefore this example necessarily has $\iint|f|\,dx\,dy = \infty$: near the origin $|f(x,y)| \sim \frac{x^2+y^2}{(x^2+y^2)^2} = \frac{1}{x^2+y^2}$, whose integral over a small disk diverges logarithmically. So the failure is exactly the failure of the hypothesis $|f| \in L^1$.
<1>5. What Tonelli's theorem implies about such $f$.
    Proof: Tonelli's theorem applies to non-negative measurable functions and asserts that both iterated integrals (possibly infinite) are equal. It cannot apply to $f$ here because $f$ changes sign. Equivalently, Tonelli applied to $|f|$ yields $\int\!\!\int|f| = \infty$, consistent with $\int(\int|f_x|\,dy)dx = \int(\int|f_y|\,dx)dy = \infty$.
<1>6. Q.E.D.
:::
