---
schema: qual/card@1
id: P-MMAQ-DS33H2Y6F3
kind: problem
title: "Let $f, g \\in L^2(\\RR)$. Show that $\\lim _{n \\rightarrow \\infty} \\int_{\\mathbb{R}} f(x) g(x+n) d x=0$"
classification:
  areas:
  - real-analysis
  topics:
  - l2
  - convergence-of-integrals
relations: []
review: draft
---

::: problem
Let $f, g \in L^2(\RR)$.
Show that
$$
\lim _{n \rightarrow \infty} \int_{\mathbb{R}} f(x) g(x+n) d x=0
$$
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

**Goal:** Let $f, g \in L^2(\RR)$. Prove that $\lim_{n\to\infty} \int_\RR f(x) g(x+n)\,dx = 0$.

<1>1. **Compactly supported case.**
  <2>1. Suppose $f$ and $g$ have compact support: $\operatorname{supp}(f) \subseteq [-R, R]$ and $\operatorname{supp}(g) \subseteq [-R, R]$ for some $R > 0$.
  <2>2. For all $n > 2R$, $\int_\RR f(x) g(x+n)\,dx = 0$.
    Proof: If $x \in \operatorname{supp}(f)$, then $x \geq -R$, so $x + n > -R + 2R = R$. Hence $x+n \notin \operatorname{supp}(g)$, which means $g(x+n) = 0$. Thus the integrand $f(x)g(x+n)$ is identically zero everywhere on $\RR$.
  <2>3. $\lim_{n\to\infty} \int_\RR f(x) g(x+n)\,dx = 0$ for all compactly supported $f, g \in C_c(\RR)$ (or $L^2$ with compact support).

<1>2. **Density of compactly supported continuous functions in $L^2(\RR)$.**
  <2>1. Let $\eps > 0$ be given.
  <2>2. Since $C_c(\RR)$ is dense in $L^2(\RR)$, there exist $f_\eps, g_\eps \in C_c(\RR)$ such that:
    $$
    \|f - f_\eps\|_2 < \frac{\eps}{3 (\|g\|_2 + 1)} \quad \text{and} \quad \|g - g_\eps\|_2 < \frac{\eps}{3 (\|f_\eps\|_2 + 1)}.
    $$
    Proof: Standard density theorem of $C_c(\RR)$ in $L^2(\RR, \mathcal L, m)$.

<1>3. **Three-term splitting.**
  <2>1. Decompose the integral for any $n \in \NN$:
    $$
    \int_\RR f(x) g(x+n)\,dx = \int_\RR (f(x) - f_\eps(x)) g(x+n)\,dx + \int_\RR f_\eps(x) (g(x+n) - g_\eps(x+n))\,dx + \int_\RR f_\eps(x) g_\eps(x+n)\,dx.
    $$
    Proof: By linearity of the integral.
  <2>2. Bound the first term:
    $$
    \left| \int_\RR (f(x) - f_\eps(x)) g(x+n)\,dx \right| \leq \|f - f_\eps\|_2 \|g(\cdot + n)\|_2 = \|f - f_\eps\|_2 \|g\|_2 < \frac{\eps}{3}.
    $$
    Proof: By the Cauchy-Schwarz inequality in $L^2(\RR)$, and translation invariance of the $L^2$-norm: $\|g(\cdot + n)\|_2 = \|g\|_2$.
  <2>3. Bound the second term:
    $$
    \left| \int_\RR f_\eps(x) (g(x+n) - g_\eps(x+n))\,dx \right| \leq \|f_\eps\|_2 \|g(\cdot + n) - g_\eps(\cdot + n)\|_2 = \|f_\eps\|_2 \|g - g_\eps\|_2 < \frac{\eps}{3}.
    $$
    Proof: Cauchy-Schwarz inequality and translation invariance of the $L^2$-norm.
  <2>4. Bound the third term:
    There exists $N_0 \in \NN$ such that for all $n \geq N_0$, $\int_\RR f_\eps(x) g_\eps(x+n)\,dx = 0 < \frac{\eps}{3}$.
    Proof: Since $f_\eps, g_\eps \in C_c(\RR)$, by <1>1 there exists $R > 0$ such that $\operatorname{supp}(f_\eps), \operatorname{supp}(g_\eps) \subseteq [-R, R]$. Choosing $N_0 = \lceil 2R \rceil + 1$, the supports are disjoint for all $n \geq N_0$.
  <2>5. For all $n \geq N_0$:
    $$
    \left| \int_\RR f(x) g(x+n)\,dx \right| \leq \frac{\eps}{3} + \frac{\eps}{3} + 0 < \eps.
    $$
    Proof: Combining <2>1, <2>2, <2>3, and <2>4 by the triangle inequality.

<1>4. **Conclusion.**
  $\lim_{n\to\infty} \int_\RR f(x) g(x+n)\,dx = 0$. (This also expresses the fact that the shift operator sequence $T_n g = g(\cdot + n)$ converges weakly to $0$ in $L^2(\RR)$). Q.E.D.
:::
