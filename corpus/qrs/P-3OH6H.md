---
schema: qual/card@1
id: P-3OH6H
kind: problem
title: "2. Claim: take $\\delta < \\min(1, \\sqrt{\\frac{\\varepsilon}{5}})$. Then\u2026"
classification:
  areas:
  - prelim
  topics:
  - limits
  - continuity
relations: []
review: draft
solved: true
---

::: problem
2. Claim: take $\delta < \min(1, \sqrt{\frac{\varepsilon}{5}})$. Then $\abs{x-2} < \delta \implies 1 < x < 2 \implies 1 > \frac 1 x > \frac 1 2$, so in particular $\frac 1 x < 1$ and
   $$\begin{align*}
   \abs{x + \frac 1 x - \frac 5 2} &= \abs{\frac{2x^2 - 5x + 2}{2x}}\\
   &< \frac 1 2 \abs{(2x^2-4x + 2) - x}\\
   &= \frac 1 2 \abs{2(x-2)^2 + 3(x-2)} \\
   &< \abs{2(x-2)^2 + 3(x-2)} \\
   &\leq 2\abs{x-2}^2 + 3\abs{x-2} \\
   &< 2\delta^2 + 3\delta \\ 
   &< 5\delta^2  \hspace{10em} \text{since } \delta < 1 \implies \delta^2 < \delta \\
   &< 5 \left(\sqrt{\frac{\varepsilon}{5}}\right)^2 \\
   &= \varepsilon.
   \end{align*}$$
   $\qed$
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

**Goal:** Prove using the $\varepsilon$-$\delta$ definition of limit that $\lim_{x \to 2} \left(x + \frac{1}{x}\right) = \frac{5}{2}$.

<1>1. Let $\varepsilon > 0$ be arbitrary. Define $\delta = \min\left(1, \, \frac{\varepsilon}{4}\right)$.
    Proof: Since $\varepsilon > 0$, $\delta > 0$.

<1>2. Assume $0 < |x - 2| < \delta$. Then $1 < x < 3$ and in particular $|x| > 1$.
    Proof: By $|x - 2| < \delta \le 1$, we have $-1 < x - 2 < 1$, which gives $1 < x < 3$. Since $x > 1$, $|x| > 1$ and thus $\frac{1}{|x|} < 1$.

<1>3. For all $x \neq 0$, $\left|\left(x + \frac{1}{x}\right) - \frac{5}{2}\right| = \frac{|2x - 1| \cdot |x - 2|}{2|x|}$.
    Proof: Direct algebraic simplification:
    $$\left(x + \frac{1}{x}\right) - \frac{5}{2} = \frac{2x^2 - 5x + 2}{2x} = \frac{(2x - 1)(x - 2)}{2x}.$$
    Taking absolute values gives the identity.

<1>4. Under $0 < |x - 2| < \delta$, $\frac{|2x - 1| \cdot |x - 2|}{2|x|} < \varepsilon$.
    Proof:
    <2>1. $|2x - 1| < 5$.
        Proof: Since $1 < x < 3$, multiplying by $2$ and subtracting $1$ gives $1 < 2x - 1 < 5$, so $|2x - 1| < 5$.
    <2>2. $\frac{1}{2|x|} < \frac{1}{2}$.
        Proof: Since $|x| > 1$ by <1>2, $\frac{1}{2|x|} < \frac{1}{2(1)} = \frac{1}{2}$.
    <2>3. $\frac{|2x - 1|}{2|x|} < \frac{5}{2} < 4$.
        Proof: By <2>1 and <2>2, $\frac{|2x - 1|}{2|x|} < 5 \cdot \frac{1}{2} = \frac{5}{2} < 4$.
    <2>4. $\frac{|2x - 1| \cdot |x - 2|}{2|x|} < 4 |x - 2| < 4\delta \le 4\left(\frac{\varepsilon}{4}\right) = \varepsilon$.
        Proof: Follows from <2>3 and the choice $\delta \le \frac{\varepsilon}{4}$.

<1>5. Conclusion: For every $\varepsilon > 0$, there exists $\delta > 0$ such that $0 < |x - 2| < \delta \implies \left|\left(x + \frac{1}{x}\right) - \frac{5}{2}\right| < \varepsilon$.
    Proof: Follows from <1>1 through <1>4. Q.E.D.
:::
