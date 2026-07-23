---
schema: qual/card@1
id: P-3FK2S
kind: problem
title: "Let $\\varphi$ be a compactly supported smooth function that vanishes o\u2026"
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
---
Let $\varphi$ be a compactly supported smooth function that vanishes outside of an interval $[-N, N]$ such that $\int _{\RR} \varphi(x) \, dx = 1$.

For $f\in L^1(\RR)$, define
\[
K_{j}(x) \definedas j \varphi(j x), 
\qquad 
f \ast K_{j}(x) \definedas \int_{\RR} f(x-y) K_{j}(y) \, dy
\]
and prove the following:

1. Each $f\ast K_j$ is smooth and compactly supported.

2. 
\[
\lim _{j \to \infty} \norm{f * K_{j}-f}_{1} = 0
\]

> Hint:
\[
\lim _{y \to 0} \int _{\RR} |f(x-y)-f(x)| dy = 0
\]

\todo[inline]{Add concepts.}

:::{.solution}
\hfill
:::{.concept}
\hfill
- ?
:::


**Part a**

**Lemma:** If $\varphi \in C_c^1$, then
$(f \ast \varphi)' = f \ast \varphi'$ almost everywhere.

*Silly Proof:*

\[
\mathcal{F}(
	(f \ast \varphi)'
 )
&= 2\pi i \xi ~\mathcal{F}(f\ast \varphi) \\
&= 2\pi i \xi ~ \mathcal{F}(f) ~ \mathcal{F}(\varphi) \\
&= \mathcal{F}(f) \cdot \left( 2\pi i \xi ~\mathcal{F}(\varphi)\right) \\
&= \mathcal{F}(f) \cdot \mathcal{F}(\varphi') \\
&= \mathcal{F}(f\ast \varphi')
.\]

*Actual proof*:

\[
(f\ast \varphi)'(x)
&= (\varphi\ast f)'(x) \\
&= \lim_{h\to 0} \frac{(\varphi\ast f)'(x+h) - (\varphi\ast f)'(x)}{h} \\
&= \lim_{h\to 0} \int \frac{\varphi(x + h - y) - \varphi(x - y)}{h} f(y) \\
&\overset{DCT}=  \int \lim_{h\to 0} \frac{\varphi(x + h - y) - \varphi(x - y)}{h} f(y) \\
&= \int \varphi'(x-y) f(y) \\
&= (\varphi' \ast f)(x) \\
&= (f \ast \varphi')(x)
.\]
 

 To see that the DCT is justified, we can apply the MVT on the interval $[0, h]$ to $f$ to obtain

\[
\frac{\varphi(x + h - y) - \varphi(x - y)}{h}
&= \varphi'(c) \quad c\in [0, h]
,\]
 
and since $\varphi'$ is continuous and compactly supported, $\varphi'$ is bounded by some $M < \infty$ by the extreme value theorem and thus
\[
\int \abs{\frac{\varphi(x + h - y) - \varphi(x - y)}{h} f(y)} 
&= \int \abs{\varphi'(c) f(y)} \\
&\leq \int \abs{M}\abs{f} \\
&= \abs{M} \int \abs{f} < \infty
,\]

since $f\in L^1$ by assumption, so we can take $g\definedas \abs{M} \abs{f}$ as the dominating function.

Applying this theorem infinitely many times shows that $f\ast \varphi$ is smooth.

To see that $f\ast \varphi$ is compactly supported, approximate $f$ by a *continuous* compactly supported function $h$, so $\norm{h - f}_1 \converges{L^1}\to 0$. 

Now let $g_x(y) = \varphi(x-y)$, and note that $\mathrm{supp}(g) = x - \mathrm{supp}(\varphi)$ which is still compact.
 
But since $\mathrm{supp}(h)$ is bounded, there is some $N$ such that 
$$
\abs{x} > N \implies A_x\definedas \mathrm{supp}(h) \intersect \mathrm{supp}(g_x) = \emptyset
$$

and thus 
\[
(h\ast \varphi)(x) 
&= \int_\RR \varphi(x-y) h(y)~dy \\
&= \int_{A_x} g_x(y) h(y) \\
&= 0
,\]

so $\theset{x \suchthat f\ast g(x) = 0}$ is open, and its complement is closed and bounded and thus compact.

**Part b**

\[
\norm{f\ast K_j - f}_1 
&= \int \abs{\int f(x-y) K_j(y) ~dy  - f(x)}~dx \\
&= \int \abs{\int f(x-y) K_j(y) ~dy  - \int f(x) K_j(y) ~ dy}~dx \\
&= \int \abs{\int ( f(x-y) - f(x) ) K_j(y) ~dy } ~dx \\
&\leq \int \int \abs{(f(x-y) - f(x))} \cdot \abs{K_j(y)} ~ dy~dx \\
&\overset{FT}= \int \int \abs{(f(x-y) - f(x))} \cdot \abs{K_j(y)} \mathbf{~ dx~dy}\\
&= \int \abs{K_j(y)} \left( \int \abs{(f(x-y) - f(x))}  ~ dx\right) ~dy \\
&= \int \abs{K_j(y)} \cdot \norm{f - \tau_y f}_1 ~dy
.\]

We now split the integral up into pieces. 

1. Chose $\delta$ small enough such that
 $\abs{y} < \delta \implies \norm{f - \tau_y f}_1 < \varepsilon$ by continuity of translation in $L^1$, and

2. Since $\varphi$ is compactly supported, choose $J$ large enough such that
$$
j > J \implies \int_{\abs{y} \geq \delta} \abs{K_j(y)} ~dy 
= \int_{\abs{y} \geq \delta} \abs{j\varphi(jy)} = 0
$$

Then
\[
\norm{f\ast K_j - f}_1 
&\leq 
\int \abs{K_j(y)} \cdot \norm{f - \tau_y f}_1 ~dy \\
&= \int_{\abs y < \delta} \abs{K_j(y)} \cdot \norm{f - \tau_y f}_1 ~dy+ \int_{\abs y \geq  \delta} \abs{K_j(y)} \cdot \norm{f - \tau_y f}_1 ~dy \\
&= \varepsilon \int_{\abs y \geq  \delta} \abs{K_j(y)} + 0 \\
&\leq \varepsilon(1) \to 0
.\]


:::



