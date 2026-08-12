# $L^p$ Spaces

:::{.warnings}
$L^p$ convergence does not imply pointwise convergence or even a.e. convergence -- instead, if $f_k\to f$ in $L^p$, there is some *subsequence* that converges to $f$ a.e.

:::

[[PR-NFB7Q]]

[[T-4KKSH]]

:::{.proof title="?"}
Let $M = \norm{f}_\infty$.

- For any $L < M$, let $S = \theset{\abs{f} \geq L}$. 
- Then $m(S) > 0$ and

\[
\pnorm{f}p 
&= \left( \int_X \abs{f}^p \right)^{\frac 1 p} \\
&\geq \left( \int_S \abs{f}^p \right)^{\frac 1 p} \\
&\geq L ~m(S)^{\frac 1 p} \converges{p\to\infty}\to L \\
&\implies \liminf_p \pnorm{f}p \geq M
.\]

We also have
\[
\pnorm{f}p 
&=  \left( \int_X \abs{f}^p \right)^{\frac 1 p} \\
&\leq \left( \int_X M^p \right)^{\frac 1 p} \\
&= M ~m(X)^{\frac 1 p} \mapsvia{p\to\infty} M \\
&\implies \limsup_p \pnorm{f}p \leq M
.\]

:::

[[T-5BFVS]]

:::{.proof title="$p=1$ case"}
?
:::



:::{.proof title="$p=2$ case"}
Use Riesz Representation for Hilbert spaces.
:::

[[PR-N7YFV]]

[[PR-TWF4F]]

:::{.proof title="?"}
*Proof:* Apply Fatou to $\abs{f}^p$:
\[
\int \abs{f}^p = \int \liminf \abs{f_k}^p \leq \liminf \int \abs{f_k}^p = M
.\]
:::

[[PR-JX4YU]]

:::{.proof title="?"}
Take $g_k \in C_c^0 \to f$, then $g$ is uniformly continuous, so
\[
\norm{\tau_h f - f}_p
\leq \norm{\tau_h f - \tau_h g}_p + \norm{\tau_h g - g}_p + \norm{g - f}_p \to 0
.\]
:::

[[PR-3W4FO]]

:::{.proof title="?"}
Use Young's inequality
\[
\norm{\tau_h(f\ast g) - f\ast g}_\infty
&= \norm{(\tau_h f - f) \ast g}_\infty \leq \norm{\tau_hf - f}_p \norm{g}_q \to 0
.\]

:::

# $L^1$ Facts
[[PR-HFYSO]]
:::{.proof}
\envlist

- Obvious for simple functions:
  - If $f(x) = \sum_{j=1}^n c_j \chi_{E_j}$, then $\int f = 0$ iff for each $j$, either $c_j=0$ or $m(E_j) = 0$.
  - Since nonzero $c_j$ correspond to sets where $f\neq 0$, this says $m\qty{\theset{f\neq 0}} = 0$.
- $\impliedby$:
  - If $f= 0$ almost everywhere and $\phi \nearrow f$, then $\phi = 0$ almost everywhere since $\phi(x) \leq f(x)$
  -Then
  \[
  \int f = \sup_{\phi \leq f} \int \phi = \sup_{\phi \leq f} 0 = 0
  .\]
- $\implies$:
  - Instead show negating "$f=0$ almost everywhere" implies $\int f \neq 0$.
  - Write $\theset{f\neq 0} = \union_{n\in \NN} S_n$ where $S_n \definedas \theset{x\suchthat f(x) \geq {1\over n}}$.
  - Since "not $f=0$ almost everywhere", there exists an $n$ such that $m(S_n) > 0$.
  - Then
  \[
  0 < {1\over n} \chi_{E_n} \leq f \implies
  0 < \int {1\over n} \chi_{E_n} \leq \int f
  .\]
:::
[[PR-XAVMU]]
:::{.proof}
\envlist

- Let $E\subseteq X$; for characteristic functions,
\[
\int_X \chi_E(x+h)
= \int_{X} \chi_{E+h}(x) = m(E+h) = m(E) = \int_X \chi_E(x)
\]
  by translation invariance of measure.
- So this also holds for simple functions by linearity.
- For $f\in L^+$, choose $\phi_n \nearrow f$ so $\int \phi_n \to \int f$.
- Similarly, $\tau_h \phi_n \nearrow \tau_h f$ so $\int \tau_h f \to \int f$
- Finally $\theset{\int \tau_h \phi} = \theset{\int \phi}$ by step 1, and the suprema are equal by uniqueness of limits.
:::
[[PR-HLPMX]]
[[PR-EHL3O]]
:::{.warnings}
This doesn't hold for general $L^1$ functions, take any train of triangles with height 1 and summable areas.
:::
[[T-5YROQ]]
:::{.proof}
\envlist

- Approximate with compactly supported functions.
- Take $g\converges{L_1}\to f$ with $g\in C_c$
- Then choose $N$ large enough so that $g=0$ on $E\definedas B_N(0)$
- Then \[ \int_E \abs{f} \leq \int_E\abs{f-g} + \int_E \abs{g}.\]
:::
[[PR-O4AY4]]
:::{.proof title="?"}
Approximate with compactly supported functions.
Take $g\converges{L_1}\to f$, then $g \leq M$ so $\int_E{f} \leq \int_E{f-g} + \int_E g \to 0 + M \cdot m(E) \to 0$.
:::
[[PR-2KEIE]]
:::{.proof title="?"}
Idea: Split up domain
Let $A = \theset{f(x) = \infty}$, then $\infty > \int f = \int_A f + \int_{A^c} f = \infty \cdot m(A) + \int_{A^c} f \implies m(X) =0$.
:::
[[T-G543T]]
:::{.proof}
\envlist

Approximate with compactly supported functions.
Take $g\converges{L_1}\to f$ with $g\in C_c$.
\[
\int f(x+h) - f(x)
&\leq \int f(x+h) - g(x+h) + \int g(x+h) - g(x) + \int g(x) - f(x) \\
&\converges{?\to?}\to 2 \varepsilon + \int g(x+h) - g(x) \\
&= \int_K g(x+h) - g(x) + \int_{K^c} g(x+h) - g(x)\\
&\converges{??}\to 0
,\]
which follows because we can enlarge the support of $g$ to $K$ where the integrand is zero on $K^c$, then apply uniform continuity on $K$.
:::
[[PR-TNFL4]]
:::{.proof title="?"}
Fubini-Tonelli, and sketch region to change integration bounds.
:::
[[T-S3C3S]]
:::{.proof title="?"}
Fubini-Tonelli, and sketch region to change integration bounds, and continuity in $L^1$.
:::
# Lp Facts
