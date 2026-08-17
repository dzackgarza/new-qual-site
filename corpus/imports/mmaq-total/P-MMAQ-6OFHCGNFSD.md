---
schema: qual/card@1
id: P-MMAQ-6OFHCGNFSD
kind: problem
title: "Let $f(z) \\in H({\\mathbb D})$, $\\text{Re}(f(z)) >0$, $f(0)= a>0$. Show that $\\abs{ \\frac{f(z)-a}{f(z)+a}} \\leq |z|, \\; \\; \\; |f'(0)| \\leq 2a$"
classification:
  areas:
  - complex-analysis
  topics:
  - schwarz-lemma
  - conformal-maps
  - fractional-linear-transformations
relations: []
review: draft
solved: true
---

::: problem
(1) Let $f(z) \in H({\mathbb D})$, $\text{Re}(f(z)) >0$, $f(0)= a>0$.
Show that $$\abs{ \frac{f(z)-a}{f(z)+a}} \leq |z|, \; \; \;
|f'(0)| \leq 2a.$$

(2) Show that the above is still true if $\text{Re}(f(z)) >0$ is replaced with $\text{Re}(f(z)) \geq 0$.
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

**Goal:**

1. Let $f \in H(\mathbb{D})$ with $\text{Re}(f(z)) > 0$ on $\mathbb{D}$ and $f(0) = a > 0$.
   Prove that $\left|\frac{f(z)-a}{f(z)+a}\right| \leq |z|$ for all $z \in \mathbb{D}$, and that $|f'(0)| \leq 2a$.

2. Prove that the inequalities remain valid under the relaxed condition $\text{Re}(f(z)) \geq 0$ on $\mathbb{D}$.

* * *

### Part 1: Strict Positivity $\text{Re}(f(z)) > 0$

<1>1. **Define the auxiliary function $g(z) = \phi_a(f(z)) = \frac{f(z) - a}{f(z) + a}$.** <2>1. Consider the Möbius transformation $\phi_a(w) = \frac{w - a}{w + a}$.
*Proof:* Algebraic definition.
<2>2. $\phi_a$ maps the right half-plane $\mathbb{H}_R = \{w \in \mathbb{C} : \text{Re}(w) > 0\}$ conformally onto the open unit disk $\mathbb{D}$.
*Proof:* For $w = u+iv$ with $u > 0$, $|w-a|^2 = (u-a)^2 + v^2 = u^2 - 2au + a^2 + v^2$, and $|w+a|^2 = (u+a)^2 + v^2 = u^2 + 2au + a^2 + v^2$.
Since $a > 0$ and $u > 0$, $4au > 0$, so $|w-a|^2 < |w+a|^2 \implies |\phi_a(w)| < 1$.
<2>3. Since $f(z) \in \mathbb{H}_R$ for all $z \in \mathbb{D}$, $g(z) = \frac{f(z) - a}{f(z) + a}$ is a holomorphic mapping from $\mathbb{D}$ into $\mathbb{D}$ (i.e. $g \in H(\mathbb{D})$ and $|g(z)| < 1$). *Proof:* Composition of holomorphic functions $f: \mathbb{D} \to \mathbb{H}_R$ and $\phi_a: \mathbb{H}_R \to \mathbb{D}$.
<2>4. $g(0) = \frac{f(0) - a}{f(0) + a} = \frac{a - a}{a + a} = 0$.
*Proof:* Hypothesis $f(0) = a$.
<2>5. Q.E.D.

<1>2. **Apply the Schwarz Lemma to $g(z)$.** <2>1. By the Schwarz Lemma applied to $g: \mathbb{D} \to \mathbb{D}$ with $g(0) = 0$: $$|g(z)| \leq |z| \quad \text{for all } z \in \mathbb{D}, \qquad \text{and} \qquad |g'(0)| \leq 1.$$ *Proof:* Standard Schwarz Lemma hypotheses are satisfied by <1>1. <2>2. Therefore, $\left|\frac{f(z) - a}{f(z) + a}\right| = |g(z)| \leq |z|$ for all $z \in \mathbb{D}$.
*Proof:* Definition of $g(z)$.
<2>3. Q.E.D.

<1>3. **Deduce the derivative bound $|f'(0)| \leq 2a$.** <2>1. By the chain rule, $g'(0) = \phi_a'(f(0)) \cdot f'(0) = \phi_a'(a) \cdot f'(0)$.
*Proof:* Differentiation of composite function.
<2>2. $\phi_a'(w) = \frac{1(w+a) - (w-a)1}{(w+a)^2} = \frac{2a}{(w+a)^2}$.
*Proof:* Quotient rule.
<2>3. At $w = a$, $\phi_a'(a) = \frac{2a}{(2a)^2} = \frac{1}{2a}$.
*Proof:* Evaluation at $w = a$.
<2>4. Thus $g'(0) = \frac{f'(0)}{2a}$.
Since $|g'(0)| \leq 1$, we obtain $\frac{|f'(0)|}{2a} \leq 1 \implies |f'(0)| \leq 2a$.
*Proof:* Substitution of <2>3 into <1>2.<2>1. <2>5. Q.E.D.

* * *

### Part 2: Non-negative Real Part $\text{Re}(f(z)) \geq 0$

<1>4. **If $\text{Re}(f(z)) \geq 0$ on $\mathbb{D}$ with $f(0) = a > 0$, then either $\text{Re}(f(z)) > 0$ everywhere or $f$ is constant.** <2>1. The real part $u(x,y) = \text{Re}(f(z))$ is a non-negative harmonic function on the open connected disk $\mathbb{D}$.
*Proof:* Real parts of holomorphic functions are harmonic.
<2>2. By the Strong Minimum Principle for harmonic functions, since $u(0,0) = a > 0$, if there exists any $z_1 \in \mathbb{D}$ such that $u(z_1) = 0$ (a minimum value $0$), then $u$ must be identically constant on $\mathbb{D}$.
*Proof:* Strong Maximum/Minimum Principle for harmonic functions on connected domains.
<2>3. Case A: If $u(z) > 0$ for all $z \in \mathbb{D}$, then Part 1 applies directly, giving the desired inequalities.
*Proof:* By Part 1. <2>4. Case B: If $u(z)$ attains $0$, then $u(z) \equiv 0$ on $\mathbb{D}$, which contradicts $u(0) = a > 0$.
Hence this case cannot occur.
*Proof:* $u(0) = a > 0 \neq 0$.
<2>5. Therefore, $\text{Re}(f(z)) > 0$ holds automatically for all $z \in \mathbb{D}$, so the exact same bounds $\left|\frac{f(z)-a}{f(z)+a}\right| \leq |z|$ and $|f'(0)| \leq 2a$ hold.
*Proof:* Follows from <2>3 and <2>4. <2>6. Q.E.D.
:::
