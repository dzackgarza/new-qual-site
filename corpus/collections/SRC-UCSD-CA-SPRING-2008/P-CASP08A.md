---
schema: qual/card@1
id: P-CASP08A
kind: problem
title: "Statement and proof of Schwarz's Lemma"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
State and prove **Schwarz's Lemma** for holomorphic functions on the unit disk.
:::

::: solution
**Goal:** State Schwarz's Lemma and prove its bounds and rigidity statements using the Maximum Modulus Principle.

<1>1. Statement of Schwarz's Lemma:
    *Proof:*
    <2>1. Let $\mathbb{D} = \{ z \in \mathbb{C} \mid |z| < 1 \}$ be the open unit disk in the complex plane.
    <2>2. Let $f: \mathbb{D} \to \mathbb{C}$ be a holomorphic function satisfying:
        - $f(0) = 0$,
        - $|f(z)| \le 1$ for all $z \in \mathbb{D}$.
    <2>3. Then:
        (1) $|f(z)| \le |z|$ for all $z \in \mathbb{D}$, and
        (2) $|f'(0)| \le 1$.
    <2>4. Furthermore, if $|f(z_0)| = |z_0|$ for some non-zero $z_0 \in \mathbb{D} \setminus \{0\}$, or if $|f'(0)| = 1$, then $f$ is a rotation:
        $$f(z) = e^{i\theta} z \quad \text{for some constant } \theta \in \mathbb{R}.$$

<1>2. Proof of Part (1) and (2) (Auxiliary Function $g(z) = f(z)/z$):
    *Proof:*
    <2>1. Define the auxiliary function $g: \mathbb{D} \to \mathbb{C}$ by:
        $$g(z) \coloneqq \begin{cases} \dfrac{f(z)}{z} & \text{if } z \in \mathbb{D} \setminus \{0\}, \\ f'(0) & \text{if } z = 0. \end{cases}$$
    <2>2. Since $f$ is holomorphic on $\mathbb{D}$ and $f(0) = 0$, the Taylor series of $f$ around 0 has the form $f(z) = a_1 z + a_2 z^2 + \cdots$ with $a_1 = f'(0)$.
    <2>3. Thus $g(z) = a_1 + a_2 z + \cdots$ is **holomorphic on all of $\mathbb{D}$** (the singularity at $z = 0$ is removable).
    <2>4. Fix an arbitrary $r \in (0, 1)$ and consider the closed disk $\overline{D_r} = \{ z \in \mathbb{C} \mid |z| \le r \}$.
    <2>5. By the **Maximum Modulus Principle**, the maximum of $|g(z)|$ on $\overline{D_r}$ is attained on the boundary circle $|z| = r$:
        $$\max_{|z| \le r} |g(z)| = \max_{|z| = r} |g(z)| = \max_{|z| = r} \frac{|f(z)|}{|z|} = \frac{1}{r} \max_{|z| = r} |f(z)|.$$
    <2>6. Since $|f(z)| \le 1$ on $\mathbb{D}$, we have:
        $$|g(z)| \le \frac{1}{r} \quad \text{for all } |z| \le r.$$
    <2>7. Taking the limit as $r \to 1^-$:
        $$|g(z)| \le \lim_{r \to 1^-} \frac{1}{r} = 1 \quad \text{for all } z \in \mathbb{D}.$$
    <2>8. For any $z \in \mathbb{D} \setminus \{0\}$, $|g(z)| \le 1 \implies \frac{|f(z)|}{|z|} \le 1 \implies |f(z)| \le |z|$.
    <2>9. At $z = 0$, $|g(0)| \le 1 \implies |f'(0)| \le 1$.

<1>3. Proof of the Equality / Rigidity Case:
    *Proof:*
    <2>1. If $|f(z_0)| = |z_0|$ for some $z_0 \ne 0$, then $|g(z_0)| = 1$.
    <2>2. If $|f'(0)| = 1$, then $|g(0)| = 1$.
    <2>3. In either case, the holomorphic function $g: \mathbb{D} \to \mathbb{C}$ attains its maximum modulus ($|g(z)| = 1$) at an interior point of $\mathbb{D}$.
    <2>4. By the **Maximum Modulus Principle**, $g(z)$ must be a **constant function**:
        $$g(z) = c \quad \text{for some constant } c \in \mathbb{C} \text{ with } |c| = 1.$$
    <2>5. Since $|c| = 1$, we can write $c = e^{i\theta}$ for some $\theta \in \mathbb{R}$.
    <2>6. Therefore:
        $$f(z) = z g(z) = e^{i\theta} z.$$

<1>4. Conclusion:
    $|f(z)| \le |z|$ and $|f'(0)| \le 1$, with equality forcing $f(z) = e^{i\theta}z$. Q.E.D.
:::
