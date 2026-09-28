---
schema: qual/card@1
id: P-AZOFF-B05
kind: problem
title: Real and complex implicit function theorems for $9s^3-6st+t^2=0$
classification:
  areas: [real-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Several variables, Problem 5, in the deterministic MinerU Flash extraction assets/attachments/Azoff Problems by Topic_extracted.md.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Transcribed the statement into clean LaTeX with labelled parts against page 2 of Azoff Problems by Topic.pdf (read from the page image) and added a remark on the source typo R^x R^2 in part (c).
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Verified f(1,3)=0, f_s(1,3)=9, and f_t(1,3)=0, so both implicit function
    theorems solve locally for s as a function of t. For the requested proof
    of the complex statement from the real theorem, realified f as a map
    R^2 x R^2 -> R^2; its s-derivative is multiplication by f_s and is
    invertible. The real solution has complex-linear differential
    -(D_s f)^(-1)D_t f and is therefore holomorphic. The source compilation
    contains no worked solution.
---

::: {.problem}
Consider the polynomial function $f(s,t) = 9s^3 - 6st + t^2$. Let $P = (1,3)$.

(a) Carefully state the conclusion of the implicit function theorem concerning the equation $f(s,t) = 0$ when $f$ is considered as a function from $\mathbb{R}^2$ to $\mathbb{R}$.

(b) Carefully state the conclusion of the implicit function theorem concerning the equation $f(s,t) = 0$ when $f$ is considered as a function from $\mathbb{C}^2$ to $\mathbb{C}$.

(c) Use the implicit function theorem for functions from $\mathbb{R}^{\times}\mathbb{R}^2 \to \mathbb{R}^2$ to prove (b). (There are various approaches to this, including the definition of complex derivative, the Cauchy–Riemann equations, and consideration of total derivatives.)
:::

::: {.remark}
The source typesets the domain in part (c) as $\mathbb{R}^{\times}\mathbb{R}^2$, a typographical error.
Viewing $f$ on $\mathbb{C}^2 = \mathbb{R}^2 \times \mathbb{R}^2$ with values in $\mathbb{C} = \mathbb{R}^2$, the intended theorem is the implicit function theorem for maps $\mathbb{R}^2 \times \mathbb{R}^2 \to \mathbb{R}^2$.
:::

::: {.solution}
We have
$$
f(1,3)=9-18+9=0,
$$
and
$$
f_s(s,t)=27s^2-6t,
\qquad
f_t(s,t)=-6s+2t.
$$
Hence
$$
f_s(1,3)=9,
\qquad
f_t(1,3)=0.
$$

<1>1. Part (a): there are open intervals
$$
1\in U\subseteq\RR,
\qquad
3\in V\subseteq\RR
$$
and a unique smooth function
$$
\phi:V\longrightarrow U
$$
such that
$$
\phi(3)=1
$$
and, for $(s,t)\in U\times V$,
$$
f(s,t)=0
\quad\Longleftrightarrow\quad
s=\phi(t).
$$
Moreover,
$$
\phi'(3)=\boxed{0}.
$$

::: {.proof}
The polynomial $f:\RR^2\to\RR$ is smooth,
$$
f(1,3)=0,
$$
and the derivative with respect to the variable to be solved for satisfies
$$
f_s(1,3)=9\neq0.
$$
The real implicit function theorem therefore gives the stated neighborhoods
and unique smooth function $\phi$.

Differentiating
$$
f(\phi(t),t)=0
$$
gives
$$
f_s(\phi(t),t)\phi'(t)+f_t(\phi(t),t)=0.
$$
At $t=3$ this yields
$$
\phi'(3)
=
-\frac{f_t(1,3)}{f_s(1,3)}
=
0.
$$
:::

<1>2. Parts (b) and (c): there are open neighborhoods
$$
1\in U_{\CC}\subseteq\CC,
\qquad
3\in V_{\CC}\subseteq\CC
$$
and a unique holomorphic function
$$
\Phi:V_{\CC}\longrightarrow U_{\CC}
$$
such that
$$
\Phi(3)=1
$$
and, for $(s,t)\in U_{\CC}\times V_{\CC}$,
$$
f(s,t)=0
\quad\Longleftrightarrow\quad
s=\Phi(t).
$$
Furthermore,
$$
\Phi'(3)=0.
$$

<2>1. Realify the complex polynomial as
$$
\mathcal F:\RR^2_s\times\RR^2_t\longrightarrow\RR^2,
\qquad
\mathcal F(s,t)
=
\bigl(\Re f(s,t),\Im f(s,t)\bigr).
$$
At
$$
(s,t)=(1,3),
$$
the partial real derivative
$$
D_s\mathcal F(1,3):\RR^2\longrightarrow\RR^2
$$
is multiplication by the complex number $9$, hence is the invertible matrix
$$
9I_2.
$$

::: {.proof}
For fixed $t$, the polynomial $s\mapsto f(s,t)$ is holomorphic with complex
derivative
$$
f_s(s,t)=27s^2-6t.
$$
The real derivative of a holomorphic map $\CC\to\CC$ is the real-linear map
given by multiplication by its complex derivative. At $(1,3)$ that complex
number is $9$, so the corresponding real matrix is $9I_2$.
:::

<2>2. The real implicit function theorem gives real neighborhoods
$$
1\in U\subseteq\RR^2_s,
\qquad
3\in V\subseteq\RR^2_t
$$
and a unique $C^1$ map
$$
\Phi_{\RR}:V\longrightarrow U
$$
whose graph is exactly the zero set of $\mathcal F$ in $U\times V$.

::: {.proof}
Step <2>1 gives the invertibility hypothesis for the real implicit function
theorem applied to
$$
\mathcal F:\RR^2_s\times\RR^2_t\to\RR^2.
$$
Thus the theorem gives the stated map and local graph description.
:::

<2>3. After shrinking $U$ and $V$ if necessary,
$$
D\Phi_{\RR}(t)
=
-\bigl(D_s\mathcal F(\Phi_{\RR}(t),t)\bigr)^{-1}
D_t\mathcal F(\Phi_{\RR}(t),t)
$$
is complex-linear for every $t\in V$.

::: {.proof}
Since
$$
f_s(1,3)=9\neq0,
$$
continuity allows the neighborhoods to be chosen so that
$$
f_s(s,t)\neq0
$$
throughout $U\times V$. Differentiating
$$
\mathcal F(\Phi_{\RR}(t),t)=0
$$
gives the displayed formula.

Because $f$ is a polynomial in the complex variables $s$ and $t$, the real
maps
$$
D_s\mathcal F
\qquad\text{and}\qquad
D_t\mathcal F
$$
are multiplication by the complex numbers $f_s$ and $f_t$, respectively.
They are therefore complex-linear. The inverse of the nonzero multiplication
map $D_s\mathcal F$ is also complex-linear, so the displayed composition is
complex-linear.
:::

<2>4. Under the identifications $\RR^2\cong\CC$, the map $\Phi_{\RR}$ is
holomorphic.

::: {.proof}
Fix $t_0\in V$. Since $\Phi_{\RR}$ is real differentiable at $t_0$ and
$D\Phi_{\RR}(t_0)$ is complex-linear by step <2>3, there is
$\lambda\in\CC$ such that
$$
\Phi_{\RR}(t_0+h)-\Phi_{\RR}(t_0)
=
\lambda h+r(h),
\qquad
\frac{\abs{r(h)}}{\abs h}\longrightarrow0.
$$
For nonzero complex $h$,
$$
\frac{\Phi_{\RR}(t_0+h)-\Phi_{\RR}(t_0)}h
=
\lambda+\frac{r(h)}h
\longrightarrow
\lambda.
$$
Thus the complex derivative exists at every $t_0\in V$, so
$\Phi_{\RR}$ is holomorphic. Denote the resulting complex map by $\Phi$ and
the neighborhoods by $U_{\CC},V_{\CC}$.
:::

<2>5. The holomorphic map $\Phi$ has the graph and uniqueness stated in
step <1>2, and
$$
\Phi'(3)=0.
$$

::: {.proof}
The graph and uniqueness are exactly those supplied by the real implicit
function theorem in step <2>2, merely rewritten under
$\RR^2\cong\CC$.

Differentiating
$$
f(\Phi(t),t)=0
$$
complexly gives
$$
f_s(\Phi(t),t)\Phi'(t)+f_t(\Phi(t),t)=0.
$$
At $t=3$,
$$
\Phi'(3)
=
-\frac{f_t(1,3)}{f_s(1,3)}
=
0.
$$
:::

<2>6. Q.E.D.

::: {.proof}
Steps <2>1--<2>5 derive the complex implicit-function conclusion in step
<1>2 entirely from the real implicit function theorem, as required in part
(c).
:::

<1>3. Q.E.D.

::: {.proof}
Step <1>1 gives the real conclusion in part (a), while step <1>2 and its
substeps give the complex conclusion in part (b) and the requested real-IFT
proof in part (c).
:::
:::
