---
schema: qual/card@1
id: P-APAS04L
kind: problem
title: Radical identities for ideals and radical-membership computations
classification:
  areas:
  - applied-algebra
  topics:
  - Commutative Algebra
  - Ideals
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
Let $I$ and $J$ be ideals in the polynomial ring $R = k[x_1, \dots, x_n]$ where $k$ is a field.

(a) Show that $\sqrt{\sqrt{I}} = \sqrt{I}$.
(b) Show that $\sqrt{I \cap J} = \sqrt{IJ} = \sqrt{I} \cap \sqrt{J}$.
(c) Is $x^2 - y^2 \in \sqrt{\langle x^2 + x, x^2 - y \rangle}$ in $k[x, y]$?
(d) Is $x^2 + y^2 \in \sqrt{\langle x + y, x^2 - y \rangle}$ in $k[x, y]$?
:::

::: solution
**Goal:** Prove fundamental radical ideal identities in commutative algebra and evaluate radical membership for polynomial ideals.

<1>1. Part (a): Idempotency of Radical $\sqrt{\sqrt{I}} = \sqrt{I}$:
    *Proof:*
    <2>1. **$(\supseteq)$:** Since $I \subseteq \sqrt{I}$, applying the monotone radical operation gives $\sqrt{I} \subseteq \sqrt{\sqrt{I}}$.
    <2>2. **$(\subseteq)$:** Let $f \in \sqrt{\sqrt{I}}$.
    <2>3. By definition of radical, there exists an integer $m \ge 1$ such that $f^m \in \sqrt{I}$.
    <2>4. In turn, since $f^m \in \sqrt{I}$, there exists an integer $p \ge 1$ such that $(f^m)^p = f^{mp} \in I$.
    <2>5. Since $mp \ge 1$ is an integer and $f^{mp} \in I$, by definition $f \in \sqrt{I}$.
    <2>6. Thus $\sqrt{\sqrt{I}} = \sqrt{I}$.

<1>2. Part (b): Product and Intersection Identity $\sqrt{I \cap J} = \sqrt{IJ} = \sqrt{I} \cap \sqrt{J}$:
    *Proof:*
    <2>1. **Containments among ideals:**
        Since $IJ \subseteq I \cap J$, by monotonicity $\sqrt{IJ} \subseteq \sqrt{I \cap J}$.
    <2>2. **Proof that $\sqrt{I \cap J} \subseteq \sqrt{I} \cap \sqrt{J}$:**
        Let $f \in \sqrt{I \cap J}$. There exists $m \ge 1$ such that $f^m \in I \cap J$, so $f^m \in I$ (meaning $f \in \sqrt{I}$) and $f^m \in J$ (meaning $f \in \sqrt{J}$).
        Hence $f \in \sqrt{I} \cap \sqrt{J}$.
    <2>3. **Proof that $\sqrt{I} \cap \sqrt{J} \subseteq \sqrt{IJ}$:**
        Let $f \in \sqrt{I} \cap \sqrt{J}$.
        Then there exist integers $p, q \ge 1$ such that $f^p \in I$ and $f^q \in J$.
        Consider the product:
        $$f^{p+q} = f^p \cdot f^q \in I \cdot J = IJ.$$
        Since $f^{p+q} \in IJ$, by definition $f \in \sqrt{IJ}$.
    <2>4. Combining the three containments $\sqrt{IJ} \subseteq \sqrt{I \cap J} \subseteq \sqrt{I} \cap \sqrt{J} \subseteq \sqrt{IJ}$ proves:
        $$\sqrt{I \cap J} = \sqrt{IJ} = \sqrt{I} \cap \sqrt{J}.$$

<1>3. Part (c): Is $x^2 - y^2 \in \sqrt{\langle x^2 + x, x^2 - y \rangle}$?:
    *Proof:*
    <2>1. Let $I = \langle x^2 + x, x^2 - y \rangle \subset k[x, y]$.
    <2>2. In the quotient ring $k[x, y]/I$, we have the relations $y \equiv x^2$ and $x^2 \equiv -x$.
    <2>3. Therefore, $y \equiv -x$, which implies $y^2 \equiv (-x)^2 = x^2 \equiv -x$.
    <2>4. Thus, in the quotient ring:
        $$x^2 - y^2 \equiv (-x) - (-x) = 0 \pmod I.$$
    <2>5. Since $x^2 - y^2 \in I \subseteq \sqrt{I}$ already in power 1:
        $$x^2 - y^2 \in \sqrt{I} \quad \textbf{(Yes)}.$$
    <2>6. Explicitly: $(x^2 - y^2) = (x^2 - y) - (y^2 - y) = (x^2 - y) - (y - 1)(x^2 - y) - (y + x)(x^2 + x) \in I$.

<1>4. Part (d): Is $x^2 + y^2 \in \sqrt{\langle x + y, x^2 - y \rangle}$?:
    *Proof:*
    <2>1. Let $J = \langle x + y, x^2 - y \rangle \subset k[x, y]$.
    <2>2. In the quotient ring $k[x, y]/J$, $y \equiv -x$ and $y \equiv x^2$.
    <2>3. Equating both gives $x^2 + x \equiv 0 \implies x(x + 1) \equiv 0$.
    <2>4. Now evaluate $f = x^2 + y^2$ modulo $J$:
        $$x^2 + y^2 \equiv x^2 + (-x)^2 = 2x^2 \equiv -2x \pmod J.$$
    <2>5. For any power $m \ge 1$:
        $$(x^2 + y^2)^m \equiv (-2x)^m \equiv (-2)^m x^m \equiv (-2)^m (-1)^{m-1} x \pmod J.$$
    <2>6. Consider the variety $V(J)$ over an algebraically closed field $\bar{k}$ (with $\operatorname{char}(k) \ne 2$):
        - The equations are $y = -x$ and $y = x^2$, which give $x^2 + x = 0 \implies x = 0 \text{ or } x = -1$.
        - The points in $V(J)$ are $(0, 0)$ and $(-1, 1)$.
        - Evaluating $f(x, y) = x^2 + y^2$ at the point $(-1, 1) \in V(J)$:
          $$f(-1, 1) = (-1)^2 + 1^2 = 1 + 1 = 2 \ne 0 \quad (\text{for } \operatorname{char}(k) \ne 2).$$
    <2>7. By Hilbert's Nullstellensatz, if $f \in \sqrt{J}$, then $f$ must vanish on all points of $V(J)$.
    <2>8. Since $f(-1, 1) = 2 \ne 0$, $f \notin I(V(J)) = \sqrt{J}$.
    <2>9. Thus $x^2 + y^2 \notin \sqrt{J}$ in general (specifically for $\operatorname{char}(k) \ne 2$) $\textbf{(No)}$.

<1>5. Conclusion:
    $\sqrt{\sqrt{I}} = \sqrt{I}$; $\sqrt{I \cap J} = \sqrt{IJ} = \sqrt{I} \cap \sqrt{J}$; (c) is **Yes**; (d) is **No** (unless $\operatorname{char}(k) = 2$). Q.E.D.
:::
