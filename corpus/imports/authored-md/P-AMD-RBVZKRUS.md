---
schema: qual/card@1
id: P-AMD-RBVZKRUS
kind: problem
title: "Show that $L^2([0, 1]) \u2286 L^1([0, 1])$ and argue that $L^2([0, 1])$ in fact forms a dense subset of $L^1([0, 1])$."
classification:
  areas:
  - real-analysis
  topics:
  - riesz-representation
  - lp-spaces
  - density
relations: []
review: draft
---

::: {.problem}
a.  Show that $L^2([0, 1]) ⊆ L^1([0, 1])$ and argue that $L^2([0, 1])$ in fact forms a dense subset of $L^1([0, 1])$.

b.  Let $Λ$ be a continuous linear functional on $L^1([0, 1])$.
  
    Prove the Riesz Representation Theorem for $L^1([0, 1])$ by following the steps below:


    i. Establish the existence of a function $g ∈ L^2([0, 1])$ which represents $Λ$ in the sense that
    $$
    Λ(f ) = f (x)g(x) dx \text{ for all } f ∈ L^2([0, 1]).
    $$

    > Hint: You may use, without proof, the Riesz Representation Theorem for $L^2([0, 1])$.

    ii. Argue that the $g$ obtained above must in fact belong to $L^∞([0, 1])$ and represent $Λ$ in the sense that
    $$
    \Lambda(f)=\int_{0}^{1} f(x) \overline{g(x)} d x \quad \text { for all } f \in L^{1}([0,1])
    $$
    with
    $$
    \|g\|_{L^{\infty}([0,1])}=\|\Lambda\|_{L^{1}([0,1])\dual}
    $$
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

**Goal:** Prove that $L^2([0, 1]) \subseteq L^1([0, 1])$ is dense, and establish the Riesz Representation Theorem $(L^1([0, 1]))^* \cong L^\infty([0, 1])$ using the $L^2$ Riesz Representation Theorem.

<1>1. **Part (a): $L^2([0, 1]) \subseteq L^1([0, 1])$ and $L^2([0, 1])$ is dense in $L^1([0, 1])$.**
  <2>1. $L^2([0, 1]) \subseteq L^1([0, 1])$ with $\|f\|_1 \leq \|f\|_2$ for all $f \in L^2([0, 1])$.
    Proof: Let $f \in L^2([0, 1])$. By Cauchy-Schwarz inequality with the constant function $1 \in L^2([0, 1])$:
    $$
    \|f\|_1 = \int_0^1 |f(x)| \cdot 1\,dx \leq \left(\int_0^1 |f(x)|^2\,dx\right)^{1/2} \left(\int_0^1 1^2\,dx\right)^{1/2} = \|f\|_2 \cdot 1 = \|f\|_2.
    $$
    Thus $f \in L^1([0, 1])$.
  <2>2. $L^2([0, 1])$ is dense in $L^1([0, 1])$.
    Proof: The space of simple functions $\mathcal S = \left\{\sum_{j=1}^m c_j \chi_{E_j} : m \in \NN, E_j \subseteq [0, 1] \text{ measurable}\right\}$ is dense in $L^1([0, 1])$. Furthermore, every simple function $\phi \in \mathcal S$ is bounded on $[0, 1]$, so $\int_0^1 |\phi|^2\,dx \leq (\max |\phi|)^2 < \infty$, which means $\mathcal S \subseteq L^2([0, 1])$. Since $\mathcal S \subseteq L^2([0, 1]) \subseteq L^1([0, 1])$ and $\overline{\mathcal S}^{\|\cdot\|_1} = L^1([0, 1])$, the intermediate space $L^2([0, 1])$ is dense in $L^1([0, 1])$ in the $L^1$-norm.

<1>2. **Part (b)(i): Existence of $g \in L^2([0, 1])$ representing $\Lambda$ on $L^2([0, 1])$.**
  <2>1. The restriction $\Lambda|_{L^2}$ is a bounded (continuous) linear functional on the Hilbert space $L^2([0, 1])$.
    Proof: $\Lambda$ is linear. For any $f \in L^2([0, 1])$, by continuity of $\Lambda$ on $L^1([0, 1])$ and <2>1:
    $$
    |\Lambda(f)| \leq \|\Lambda\|_{(L^1)^*} \|f\|_1 \leq \|\Lambda\|_{(L^1)^*} \|f\|_2.
    $$
    Thus $\Lambda|_{L^2}$ is continuous on $L^2([0, 1])$ with $\|\Lambda|_{L^2}\|_{(L^2)^*} \leq \|\Lambda\|_{(L^1)^*}$.
  <2>2. By the Riesz Representation Theorem for Hilbert spaces, there exists a unique $g \in L^2([0, 1])$ such that $\Lambda(f) = \int_0^1 f(x) \overline{g(x)}\,dx$ for all $f \in L^2([0, 1])$.
    Proof: $L^2([0, 1])$ is a Hilbert space with inner product $\langle f, g \rangle = \int_0^1 f(x)\overline{g(x)}\,dx$. The Riesz Representation Theorem guarantees the existence and uniqueness of $g \in L^2([0, 1])$ satisfying $\Lambda(f) = \langle f, g \rangle$.

<1>3. **Part (b)(ii): $g \in L^\infty([0, 1])$, $\|g\|_\infty = \|\Lambda\|_{(L^1)^*}$, and $\Lambda(f) = \int_0^1 f \overline{g}\,dx$ for all $f \in L^1([0, 1])$.**
  <2>1. $\|g\|_\infty \leq \|\Lambda\|_{(L^1)^*}$, hence $g \in L^\infty([0, 1])$.
    <3>1. Suppose for contradiction that for some $M > \|\Lambda\|_{(L^1)^*}$, the set $E = \{x \in [0, 1] : |g(x)| > M\}$ has positive Lebesgue measure $m(E) > 0$.
    <3>2. Define $f_0(x) = \operatorname{sgn}(g(x)) \chi_E(x)$ (where $\operatorname{sgn}(z) = \frac{z}{|z|}$ if $z \neq 0$ and $0$ if $z = 0$).
    <3>3. $f_0 \in L^2([0, 1])$ and $\|f_0\|_1 = m(E) > 0$.
      Proof: $|f_0(x)| \leq 1$, so $f_0 \in L^\infty([0, 1]) \subseteq L^2([0, 1])$, and $\int_0^1 |f_0|\,dx = m(E)$.
    <3>4. $\Lambda(f_0) = \int_0^1 f_0 \overline{g}\,dx = \int_E |g(x)|\,dx \geq M m(E) > \|\Lambda\|_{(L^1)^*} m(E) = \|\Lambda\|_{(L^1)^*} \|f_0\|_1$.
      Proof: On $E$, $f_0(x)\overline{g(x)} = \frac{g(x)}{|g(x)|}\overline{g(x)} = |g(x)| > M$.
    <3>5. This contradicts the boundedness of $\Lambda$ on $L^1([0, 1])$, which requires $|\Lambda(f_0)| \leq \|\Lambda\|_{(L^1)^*} \|f_0\|_1$.
      Proof: The strict inequality $M m(E) > \|\Lambda\|_{(L^1)^*} m(E)$ directly contradicts $|\Lambda(f_0)| \leq \|\Lambda\|_{(L^1)^*} \|f_0\|_1$.
    <3>6. Thus $m(\{x : |g(x)| > M\}) = 0$ for every $M > \|\Lambda\|_{(L^1)^*}$, which implies $g \in L^\infty([0, 1])$ and $\|g\|_\infty \leq \|\Lambda\|_{(L^1)^*}$.
  <2>2. $\Lambda(f) = \int_0^1 f(x) \overline{g(x)}\,dx$ for all $f \in L^1([0, 1])$.
    Proof: Define the functional $\Phi(f) = \int_0^1 f(x)\overline{g(x)}\,dx$. Since $g \in L^\infty([0, 1])$, Hölder's inequality shows $|\Phi(f)| \leq \|g\|_\infty \|f\|_1$, so $\Phi$ is a continuous linear functional on $L^1([0, 1])$. By <1>2, $\Phi(f) = \Lambda(f)$ for all $f \in L^2([0, 1])$. Since $L^2([0, 1])$ is dense in $L^1([0, 1])$ (by <1>1), two continuous functionals agreeing on a dense subspace must agree on the entire space $L^1([0, 1])$.
  <2>3. $\|\Lambda\|_{(L^1)^*} \leq \|g\|_\infty$, hence $\|g\|_\infty = \|\Lambda\|_{(L^1)^*}$.
    Proof: For any $f \in L^1([0, 1])$, $|\Lambda(f)| = \left|\int_0^1 f\overline{g}\,dx\right| \leq \|g\|_\infty \|f\|_1$, which implies $\|\Lambda\|_{(L^1)^*} \leq \|g\|_\infty$. Combined with $\|g\|_\infty \leq \|\Lambda\|_{(L^1)^*}$ from <2>1, we get $\|g\|_\infty = \|\Lambda\|_{(L^1)^*}$.

<1>4. **Conclusion.**
  All parts of the problem are rigorously established. Q.E.D.
:::
