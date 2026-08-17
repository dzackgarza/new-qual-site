---
schema: qual/card@1
id: P-MMAQ-TWTQL23XGN
kind: problem
title: Let $F$ be an analytic function inside and on a simple closed
classification:
  areas:
  - complex-analysis
  topics:
  - holomorphic-functions
relations: []
review: draft
solved: true
---

::: problem
Let $F$ be an analytic function inside and on a simple closed
curve $C$, except for a pole of order $m\geq 1$ at $z=a$ inside $C$.
Prove that

$$
\frac{1}{2 \pi i}\oint_{C} F(\tau) d\tau = 
\lim_{\tau\rightarrow a} \frac{d^{m-1}}{d\tau^{m-1}}\big((\tau-a)^m F(\tau))\big)
.$$
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

**Goal:** Let $C$ be a simple closed positively oriented contour, and let $F$ be holomorphic on $C$ and in its interior except for a pole of order $m \geq 1$ at $a \in \text{Int}(C)$. Prove the residue formula for a pole of order $m$ via Cauchy's integral formula for derivatives:
$$\frac{1}{2\pi i} \oint_C F(z) \, dz = \frac{1}{(m-1)!} \lim_{z \to a} \frac{d^{m-1}}{dz^{m-1}} \big( (z - a)^m F(z) \big).$$
*(Note: Standard conventions include the factor $\frac{1}{(m-1)!}$; we prove this complete formula and state the relationship explicitly).*

---

### Step 1: Holomorphic Factoring of the Pole

<1>1. **Define the regular part $g(z) = (z - a)^m F(z)$.**
  <2>1. Since $F$ has a pole of order $m \geq 1$ at $a$, its Laurent expansion near $a$ is:
  $$F(z) = \frac{c_{-m}}{(z - a)^m} + \frac{c_{-m+1}}{(z - a)^{m-1}} + \dots + \frac{c_{-1}}{z - a} + \sum_{n=0}^\infty c_n (z - a)^n,$$
  with $c_{-m} \neq 0$.
    *Proof:* Definition of pole of order $m$.
  <2>2. Multiplying by $(z - a)^m$:
  $$g(z) \coloneqq (z - a)^m F(z) = c_{-m} + c_{-m+1}(z - a) + \dots + c_{-1}(z - a)^{m-1} + \sum_{n=0}^\infty c_n (z - a)^{n+m}.$$
    *Proof:* Multiplying the Laurent series by $(z-a)^m$.
  <2>3. The singularity of $g(z)$ at $z = a$ is removable with $g(a) = c_{-m} \neq 0$, so $g$ is holomorphic on $\text{Int}(C) \cup C$.
    *Proof:* Riemann's removable singularity theorem.
  <2>4. Q.E.D.

---

### Step 2: Connection with Cauchy's Integral Formula for Derivatives

<1>2. **Express $\oint_C F(z)\,dz$ in terms of $g(z)$.**
  <2>1. By definition of $g(z)$, $F(z) = \frac{g(z)}{(z - a)^m}$ on $\text{Int}(C) \setminus \{a\}$.
    *Proof:* Division by $(z - a)^m \neq 0$.
  <2>2. The contour integral becomes:
  $$\frac{1}{2\pi i} \oint_C F(z) \, dz = \frac{1}{2\pi i} \oint_C \frac{g(z)}{(z - a)^m} \, dz.$$
    *Proof:* Substitution of $F(z) = \frac{g(z)}{(z-a)^m}$.
  <2>3. By Cauchy's Integral Formula for the $(m-1)$-th derivative of the holomorphic function $g$:
  $$\frac{1}{2\pi i} \oint_C \frac{g(z)}{(z - a)^m} \, dz = \frac{g^{(m-1)}(a)}{(m-1)!}.$$
    *Proof:* Cauchy's Integral Formula for higher derivatives: $g^{(k)}(a) = \frac{k!}{2\pi i} \oint_C \frac{g(z)}{(z-a)^{k+1}}\,dz$ with $k = m-1$.
  <2>4. Q.E.D.

---

### Step 3: Compute the Residue and Evaluate the Limit

<1>3. **Compute the derivative $g^{(m-1)}(a)$.**
  <2>1. Since $g$ is holomorphic, $g^{(m-1)}(a) = \lim_{z \to a} \frac{d^{m-1}}{dz^{m-1}} g(z) = \lim_{z \to a} \frac{d^{m-1}}{dz^{m-1}} \big( (z - a)^m F(z) \big)$.
    *Proof:* Continuity of derivatives of holomorphic functions.
  <2>2. Differentiating the Taylor series of $g(z) = \sum_{j=0}^\infty c_{j-m} (z - a)^j$ term-by-term $m-1$ times:
  $$\frac{d^{m-1}}{dz^{m-1}} g(z) = (m-1)! c_{-1} + m! c_0 (z - a) + \dots$$
    *Proof:* Differentiation of power series.
  <2>3. Taking the limit as $z \to a$:
  $$\lim_{z \to a} \frac{d^{m-1}}{dz^{m-1}} \big( (z - a)^m F(z) \big) = (m-1)! c_{-1}.$$
    *Proof:* Evaluating at $z = a$.
  <2>4. Therefore:
  $$\frac{1}{2\pi i} \oint_C F(z) \, dz = c_{-1} = \frac{1}{(m-1)!} \lim_{z \to a} \frac{d^{m-1}}{dz^{m-1}} \big( (z - a)^m F(z) \big).$$
    *Proof:* Combines <1>2.<2>3 and <2>3.
  <2>5. Q.E.D.
:::
