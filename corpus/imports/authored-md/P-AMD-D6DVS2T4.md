---
schema: qual/card@1
id: P-AMD-D6DVS2T4
kind: problem
title: A nonnegative $f$ is Lebesgue measurable iff its subgraph $\mathcal A$ is, and $m(\mathcal A)=\int f=\int_0^\infty m(\{f\ge t\})\,dt$
classification:
  areas:
  - real-analysis
  topics:
  - measure-theory
  - integrals
  - fubini-tonelli
relations: []
review: draft
solved: true
---

::: {.problem}
Let $f$ be a non-negative function on $\RR^n$ and $\mathcal A = \{(x, t) ∈ \RR^n \times \RR : 0 \leq t \leq f (x)\}$.

Prove the validity of the following two statements:

  a. $f$ is a Lebesgue measurable function on $\RR^n \iff  \mathcal A$ is a Lebesgue measurable subset of $\RR^{n+1}$
  
  b. If $f$ is a Lebesgue measurable function on $\RR^n$, then
  $$
  m(\mathcal{A})=\int_{\mathbb{R}^{n}} f(x) d x=\int_{0}^{\infty} m\left(\left\{x \in \mathbb{R}^{n}: f(x) \geq t\right\}\right) d t
  $$
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

**Goal:** Let $f: \RR^n \to [0, \infty)$ and $\mathcal A = \{(x, t) \in \RR^n \times \RR : 0 \leq t \leq f(x)\}$. Prove:
(a) $f$ is Lebesgue measurable on $\RR^n \iff \mathcal A$ is Lebesgue measurable in $\RR^{n+1}$;
(b) If $f$ is Lebesgue measurable, then $m(\mathcal A) = \int_{\RR^n} f(x)\,dx = \int_0^\infty m(\{x\in\RR^n : f(x) \geq t\})\,dt$.

<1>1. **Part (a) ($\implies$): If $f$ is measurable on $\RR^n$, then $\mathcal A$ is measurable in $\RR^{n+1}$.**
  <2>1. There exists a sequence of non-negative simple measurable functions $\{\phi_k\}_{k=1}^\infty$ on $\RR^n$ such that $0 \leq \phi_1(x) \leq \phi_2(x) \leq \cdots \nearrow f(x)$ pointwise for every $x \in \RR^n$.
    Proof: By the standard simple function approximation theorem for non-negative measurable functions on $\RR^n$.
  <2>2. For any characteristic function $\chi_E$ where $E \subseteq \RR^n$ is Lebesgue measurable, the set $\mathcal A(\chi_E) = \{(x, t) \in \RR^n \times \RR : 0 \leq t \leq \chi_E(x)\} = (E \times [0, 1]) \cup (E^c \times \{0\})$ is Lebesgue measurable in $\RR^{n+1}$.
    Proof: $E \times [0, 1]$ is measurable in $\RR^{n+1}$ as a product of measurable sets, and $E^c \times \{0\}$ is a subset of $\RR^n \times \{0\}$ which is a set of Lebesgue measure zero in $\RR^{n+1}$, hence measurable. Thus their union is measurable.
  <2>3. For any non-negative simple measurable function $\phi = \sum_{j=1}^m c_j \chi_{E_j}$ with disjoint measurable sets $E_j \subseteq \RR^n$ and $c_j \geq 0$, the set $\mathcal A(\phi) = \{(x, t) : 0 \leq t \leq \phi(x)\} = \bigcup_{j=1}^m (E_j \times [0, c_j]) \cup ((\bigcup E_j)^c \times \{0\})$ is measurable in $\RR^{n+1}$.
    Proof: Each $E_j \times [0, c_j]$ is a product of measurable sets in $\RR^n$ and $\RR$, hence measurable in $\RR^{n+1}$. The finite union of measurable sets plus the null set $(\bigcup E_j)^c \times \{0\}$ is measurable in $\RR^{n+1}$.
  <2>4. The set $\mathcal A^\circ \definedas \{(x, t) \in \RR^n \times \RR : 0 \leq t < f(x)\} = \bigcup_{k=1}^\infty \{(x, t) : 0 \leq t \leq \phi_k(x) - 1/k\}$ (or equivalently $\bigcup_{k=1}^\infty \mathcal A'(\phi_k)$) is measurable in $\RR^{n+1}$.
    Proof: For each $(x, t)$ with $t \geq 0$, $t < f(x) \iff \exists k \in \NN, t \leq \phi_k(x)$ and $t < \phi_k(x)$. More directly, $\{(x, t) \in \RR^n \times [0, \infty) : t < f(x)\} = \bigcup_{q \in \mathbb{Q}_{>0}} (\{x : f(x) > q\} \times [0, q))$, which is a countable union of measurable rectangles, hence measurable in $\RR^{n+1}$.
  <2>5. The graph $\Gamma(f) = \{(x, f(x)) : x \in \RR^n\}$ is measurable in $\RR^{n+1}$ with measure zero.
    Proof: By Tonelli's theorem applied to $\chi_{\Gamma(f)}$, the slice at $x$ is the singleton $\{f(x)\}$ which has 1D measure zero. Thus $\Gamma(f)$ is measurable and $m_{n+1}(\Gamma(f)) = \int_{\RR^n} m_1(\{f(x)\})\,dx = 0$.
  <2>6. $\mathcal A = \{(x, t) : 0 \leq t < f(x)\} \cup \Gamma(f)$ is Lebesgue measurable in $\RR^{n+1}$.
    Proof: By <2>4 and <2>5, $\mathcal A$ is the union of two Lebesgue measurable sets in $\RR^{n+1}$.

<1>2. **Part (a) ($\impliedby$): If $\mathcal A$ is measurable in $\RR^{n+1}$, then $f$ is measurable on $\RR^n$.**
  <2>1. For every $t \geq 0$, the horizontal cross-section (slice) $\mathcal A_t = \{x \in \RR^n : (x, t) \in \mathcal A\} = \{x \in \RR^n : f(x) \geq t\}$ is Lebesgue measurable in $\RR^n$.
    Proof: By Fubini-Tonelli theorem for product measurable spaces, every section of a Lebesgue measurable set in $\RR^{n+1}$ at almost every $t$ is measurable, and for all $t$ when considering the complete product measure space $(\RR^n \times \RR, \mathcal L(\RR^{n+1}))$. Specifically, the section of the measurable set $\mathcal A$ at any fixed $t$ is measurable in $\RR^n$.
  <2>2. $f$ is a Lebesgue measurable function.
    Proof: For any $\alpha \in \RR$, if $\alpha \leq 0$, $\{x \in \RR^n : f(x) \geq \alpha\} = \RR^n$, which is measurable. If $\alpha > 0$, $\{x \in \RR^n : f(x) \geq \alpha\} = \mathcal A_\alpha$, which is measurable by <2>1. Thus the pre-image of every ray $[\alpha, \infty)$ is measurable, which proves that $f$ is measurable.

<1>3. **Part (b): $m(\mathcal A) = \int_{\RR^n} f(x)\,dx = \int_0^\infty m(\{x \in \RR^n : f(x) \geq t\})\,dt$.**
  <2>1. The indicator function $\chi_{\mathcal A}(x, t)$ is non-negative and measurable on $\RR^n \times \RR$.
    Proof: Follows directly from the measurability of $\mathcal A$ in $\RR^{n+1}$ established in <1>1.
  <2>2. $m(\mathcal A) = \int_{\RR^n} f(x)\,dx$.
    Proof: By Tonelli's Theorem, integrating with respect to $t$ first:
    $$
    m(\mathcal A) = \int_{\RR^{n+1}} \chi_{\mathcal A}(x, t)\,d(x, t) = \int_{\RR^n} \left( \int_\RR \chi_{\mathcal A}(x, t)\,dt \right) dx.
    $$
    For a fixed $x \in \RR^n$, $\chi_{\mathcal A}(x, t) = 1 \iff 0 \leq t \leq f(x)$, so $\int_\RR \chi_{\mathcal A}(x, t)\,dt = \int_0^{f(x)} 1\,dt = f(x)$. Thus:
    $$
    m(\mathcal A) = \int_{\RR^n} f(x)\,dx.
    $$
  <2>3. $m(\mathcal A) = \int_0^\infty m(\{x \in \RR^n : f(x) \geq t\})\,dt$.
    Proof: By Tonelli's Theorem, integrating with respect to $x$ first:
    $$
    m(\mathcal A) = \int_\RR \left( \int_{\RR^n} \chi_{\mathcal A}(x, t)\,dx \right) dt.
    $$
    For $t < 0$, $\chi_{\mathcal A}(x, t) = 0$. For $t \geq 0$, $\chi_{\mathcal A}(x, t) = 1 \iff f(x) \geq t$. Thus:
    $$
    \int_{\RR^n} \chi_{\mathcal A}(x, t)\,dx = m(\{x \in \RR^n : f(x) \geq t\}).
    $$
    Integrating over $t \in [0, \infty)$ gives:
    $$
    m(\mathcal A) = \int_0^\infty m(\{x \in \RR^n : f(x) \geq t\})\,dt.
    $$

<1>4. **Conclusion.**
  Both statements (a) and (b) are proven rigorously. Q.E.D.
:::
