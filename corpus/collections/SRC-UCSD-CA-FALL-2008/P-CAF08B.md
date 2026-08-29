---
schema: qual/card@1
id: P-CAF08B
kind: problem
title: "True or False: meromorphic extensions, Schwarz reflection, simple connectivity, minimum modulus, and analytic continuation"
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
For each part, determine if it is always true or sometimes false.
If true give a brief proof.
If false give a counterexample.

(a) If $f \in H(B(1; 1) \setminus \{1\})$ with $|f(z)| \leq \frac{1}{|z - 1|}$ for all $z \in B(1; 1) \setminus \{1\}$, then $f$ extends to a meromorphic (or possibly analytic) function on $B(1; 1)$.

(b) Suppose that $f \in H(\{z \in B(0; 1) : \operatorname{Re} z > 0\})$ and extends continuously to the line segment $I = \{it : -1 < t < 1\}$.
If $f(I) \subset i\mathbb{R}$, then $f$ extends to an analytic function in $B(0; 1)$.

(c) If $G \subset \mathbb{C}$ is open, connected, and simply connected, and $f \in H(G)$ with $f'(z) \neq 0$ for all $z \in G$, then $f(G)$ is also open, connected, and simply connected.

(d) Let $G \subset \mathbb{C}$ be connected and open and $f \in H(G)$ nonconstant.
If $f(z) \neq 0$ for all $z \in G$, then $|f|$ does not reach a minimum at any point in $G$.

(e) Let $f$ be an analytic function element defined in $B(1/2; 1/4)$.
Suppose that $f$ continues analytically along any path $\gamma$ from $\gamma(0) \in B(1/2; 1/4)$ to $\gamma(1) \in B(0; 1) \setminus \{0\}$.
Then there is a function $F \in H(B(0; 1) \setminus \{0\})$ such that $F|_{B(1/2; 1/4)} = f$.
:::

::: solution
**Goal:** Adjudicate each of the five complex analysis statements as True or False with rigorous proofs or explicit counterexamples.

<1>1. Part (a): **TRUE** (Meromorphic Extension via Riemann's Removable Singularity Theorem):
    *Proof:*
    <2>1. Define the auxiliary function $g(z) \coloneqq (z - 1) f(z)$ on $B(1; 1) \setminus \{1\}$.
    <2>2. By the given bound, $|g(z)| = |z - 1| |f(z)| \le |z - 1| \frac{1}{|z - 1|} = 1$ for all $z \in B(1; 1) \setminus \{1\}$.
    <2>3. Since $g$ is holomorphic and bounded near the isolated singularity $z = 1$, by **Riemann's Removable Singularity Theorem**, $g$ extends to a holomorphic function $\tilde{g}$ on all of $B(1; 1)$.
    <2>4. Thus $f(z) = \frac{\tilde{g}(z)}{z - 1}$ has at worst a **pole of order 1** at $z = 1$ (or a removable singularity if $\tilde{g}(1) = 0$).
    <2>5. Hence $f$ extends to a meromorphic function on $B(1; 1)$.

<1>2. Part (b): **TRUE** (Schwarz Reflection Principle across Imaginary Axis):
    *Proof:*
    <2>1. Consider the domain $D = \{ z \in B(0; 1) \mid \operatorname{Re}(z) > 0 \}$, bounded on the left by the imaginary segment $I = (-i, i)$.
    <2>2. Define the reflected function $F: B(0; 1) \to \mathbb{C}$ by:
        $$F(z) = \begin{cases} f(z) & \text{if } \operatorname{Re}(z) > 0, \\ f(z) & \text{if } z \in I, \\ -\overline{f(-\bar{z})} & \text{if } \operatorname{Re}(z) < 0. \end{cases}$$
    <2>3. For $z = it \in I$, $-\bar{z} = -(-it) = it = z$. Since $f(it) \in i\mathbb{R}$, $f(it) = i u$ for $u \in \mathbb{R}$, so $-\overline{f(-\bar{z})} = -\overline{iu} = -(-iu) = iu = f(it)$.
    <2>4. Thus $F(z)$ is continuous on $B(0; 1)$ and holomorphic on both the left and right semi-disks.
    <2>5. By Morera's Theorem (Schwarz Reflection Principle), $F$ is holomorphic on all of $B(0; 1)$.

<1>3. Part (c): **FALSE** (Conformal / Local Homeomorphism Need Not Have Simply Connected Image):
    *Counterexample:*
    <2>1. Let $G = \mathbb{C}$, which is open, connected, and simply connected.
    <2>2. Let $f(z) = e^z$.
    <2>3. The derivative is $f'(z) = e^z \ne 0$ for all $z \in \mathbb{C}$.
    <2>4. The image is the punctured plane $f(G) = \mathbb{C} \setminus \{0\}$.
    <2>5. The punctured plane $\mathbb{C} \setminus \{0\}$ is open and connected, but **not simply connected** ($\pi_1(\mathbb{C} \setminus \{0\}) \cong \mathbb{Z} \ne 0$).

<1>4. Part (d): **TRUE** (Minimum Modulus Principle for Non-Vanishing Holomorphic Functions):
    *Proof:*
    <2>1. Since $f \in H(G)$ and $f(z) \ne 0$ for all $z \in G$, the reciprocal function:
        $$g(z) \coloneqq \frac{1}{f(z)}$$
        is well-defined and holomorphic on the connected open set $G$.
    <2>2. Suppose for contradiction that $|f|$ attained a local minimum at some point $z_0 \in G$.
    <2>3. Then $|g(z)| = \frac{1}{|f(z)|} \le \frac{1}{|f(z_0)|} = |g(z_0)|$ for all $z$ in a neighborhood of $z_0$.
    <2>4. That is, $|g|$ attains a local maximum at $z_0 \in G$.
    <2>5. By the **Maximum Modulus Principle**, $g(z)$ must be constant on $G$, which implies $f(z) = 1/g(z)$ is constant on $G$, contradicting that $f$ is non-constant.
    <2>6. Thus $|f|$ cannot reach a minimum at any point in $G$.

<1>5. Part (e): **FALSE** (Monodromy Theorem Requires Simple Connectivity):
    *Counterexample:*
    <2>1. The domain $D = B(0; 1) \setminus \{0\}$ is the punctured unit disk, which is **not simply connected** ($\pi_1(D) \cong \mathbb{Z}$).
    <2>2. Let $f(z)$ be the branch of the complex logarithm $\operatorname{Log}(z)$ defined on $B(1/2; 1/4) \subset \{ \operatorname{Re}(z) > 0 \}$.
    <2>3. The function element $f$ can be analytically continued along any path $\gamma$ in $B(0; 1) \setminus \{0\}$.
    <2>4. However, continuing $f$ along a counterclockwise closed loop around the origin $z = 0$ changes the value by $2\pi i$ (non-trivial monodromy).
    <2>5. Thus there is no single-valued holomorphic function $F \in H(B(0; 1) \setminus \{0\})$ extending $f$.

<1>6. Conclusion:
    (a) True; (b) True; (c) False; (d) True; (e) False. Q.E.D.
:::
