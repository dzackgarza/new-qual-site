---
schema: qual/card@1
id: P-5SC3V
kind: problem
title: A PID that is not Euclidean
classification:
  areas:
  - algebra
  topics:
  - Principal Ideal Domains
  - Euclidean Domains
  - Counterexamples
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
Do you know a Principal Ideal Domain (PID) that is not a Euclidean Domain?
:::

::: solution
**Goal:** Exhibit the standard ring $R = \mathbb{Z}\left[\frac{1 + \sqrt{-19}}{2}\right]$ and prove it is a PID but not a Euclidean domain.

<1>1. Candidate Ring:
    *Proof:*
    <2>1. Consider the ring of integers of the imaginary quadratic field $K = \mathbb{Q}(\sqrt{-19})$:
        $$R = \mathcal{O}_K = \mathbb{Z}[\theta], \qquad \text{where } \theta = \frac{1 + \sqrt{-19}}{2}.$$
    <2>2. The minimal polynomial of $\theta$ is $x^2 - x + 5 = 0$, so $\theta^2 = \theta - 5$.
    <2>3. The field norm on $R$ is given by:
        $$N(a + b\theta) = \left(a + \frac{b}{2}\right)^2 + 19\left(\frac{b}{2}\right)^2 = a^2 + ab + 5b^2 \in \mathbb{Z}_{\ge 0}.$$

<1>2. Proof that $R$ is NOT a Euclidean Domain (Absence of Universal Side Divisors):
    *Proof:*
    <2>1. **Universal side divisor lemma:** In any Euclidean domain $A$ that is not a field, there exists a non-zero, non-unit element $u \in A \setminus (A^\times \cup \{0\})$ such that the reduction map $\pi: A^\times \cup \{0\} \to A/(u)$ is surjective.
    <2>2. **Units in $R$:** $N(a + b\theta) = 1 \iff a^2 + ab + 5b^2 = 1 \iff (a, b) = (\pm 1, 0)$.
        Thus the only units in $R$ are $R^\times = \{1, -1\}$.
    <2>3. Therefore, $R^\times \cup \{0\} = \{0, 1, -1\}$, which has size 3.
    <2>4. If $u$ were a universal side divisor in $R$, the residue field $R/(u)$ could have size at most $|R^\times \cup \{0\}| = 3$.
    <2>5. Since $|R/(u)| = N(u)$ for any element $u \in R$, we would need an element $u \in R$ with $N(u) = 2$ or $N(u) = 3$.
    <2>6. But the equation $a^2 + ab + 5b^2 = 2$ or $3$ has no integer solutions:
        - If $b = 0$, $a^2 = 2$ or $3$ (no integer solution).
        - If $|b| \ge 1$, $a^2 + ab + 5b^2 = \left(a + \frac{b}{2}\right)^2 + \frac{19}{4}b^2 \ge \frac{19}{4} = 4.75 > 3$.
    <2>7. Thus no such element $u$ exists, so $R$ has no universal side divisor and cannot be a Euclidean domain under *any* norm function.

<1>3. Proof that $R$ is a PID:
    *Proof:*
    <2>1. (Dedekind-Hasse criterion): An integral domain $R$ is a PID if and only if for all non-zero $a, b \in R$, either $b \mid a$ or there exist $x, y \in R$ such that $0 < N(ax - by) < N(b)$.
    <2>2. By checking cases for fractions $\frac{a}{b} \in \mathbb{Q}(\sqrt{-19})$, one always finds an appropriate element $x, y \in R$ satisfying the Dedekind-Hasse condition.
    <2>3. Alternatively, by algebraic number theory, the Minkowski bound for $K = \mathbb{Q}(\sqrt{-19})$ with discriminant $d_K = -19$ is:
        $$M_K = \frac{2}{\pi} \sqrt{19} \approx \frac{2}{3.14159} \cdot 4.3589 \approx 2.77 < 3.$$
    <2>4. The only primes below $M_K$ are $p = 2$.
    <2>5. Since the Legendre symbol $\left(\frac{-19}{2}\right) = \left(\frac{1}{2}\right)$ or checking $x^2 - x + 5 \equiv x^2 + x + 1 \pmod 2$ has no roots in $\mathbb{F}_2$, the prime 2 is inert in $K$.
    <2>6. Thus $(2)$ remains prime in $R$, so there are no non-principal ideal classes of norm $\le M_K$.
    <2>7. Hence the ideal class group is trivial: $\operatorname{Cl}(R) = 1$, which means every ideal in $R$ is principal.

<1>4. Conclusion:
    $\mathbb{Z}\left[\frac{1 + \sqrt{-19}}{2}\right]$ is a PID that is not a Euclidean domain. Q.E.D.
:::
