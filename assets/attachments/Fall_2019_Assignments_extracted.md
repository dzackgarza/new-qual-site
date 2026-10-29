<!-- page 1 -->

# Math 8100 Assignment 1

## Preliminaries

Due date: Tuesday the 27th of August 2019

1. The Cantor set $\mathcal{C}$ is the set of all $x \in [0,1]$ that have a ternary expansion $x = \sum_{k=1}^{\infty} a_k 3^{-k}$ with $a_k \neq 1$ for all $k$. Thus $\mathcal{C}$ is obtained from $[0,1]$ by removing the open middle third $(\frac{1}{3}, \frac{2}{3})$, then removing the open middle thirds $(\frac{1}{9}, \frac{2}{9})$ and $(\frac{7}{9}, \frac{8}{9})$ of the two remaining intervals, and so forth.

- (a) Find a real number $x$ belonging to the Cantor set which is not the endpoint of one of the intervals used in its construction.
- (b) Prove that $\mathcal{C}$ is both nowhere dense (and hence meager) and has measure zero.
- (c) Prove that $\mathcal{C}$ is uncountable by showing that the function $f(x) = \sum_{k=1}^{\infty} b_k 2^{-k}$ where $b_k = a_k/2$, maps $\mathcal{C}$ onto $[0, 1]$.

2. A set $A \subseteq \mathbb{R}^n$ is called an $F_\sigma$ set if it can be written as the countable union of closed subsets of $\mathbb{R}^n$. A set $B \subseteq \mathbb{R}^n$ is called a $G_\delta$ set if it can be written as the countable intersection of open subsets of $\mathbb{R}^n$.

- (a) Argue that a set is a $G_\delta$ set if and only if its complement is an $F_\sigma$ set.
- (b) Show that every closed set is a $G_\delta$ set and every open set is an $F_\sigma$ set.
Hint: One approach is to prove that every open subset of $\mathbb{R}^n$ can be written as a countable union of closed cubes with disjoint interiors. This approach is however very specific to open sets in $\mathbb{R}^n$.
- (c) Give an example of an $F_\sigma$ set which is not a $G_\delta$ set and a set which is neither an $F_\sigma$ nor a $G_\delta$ set.

3. (a) Let $\{r_n\}_{n=1}^{\infty}$ be any enumeration of all the rationals in $[0, 1]$ and define $f : [0, 1] \to \mathbb{R}$ by setting

$$f(x) = \begin{cases} \frac{1}{n} & \text{if } x = r_n \\ 0 & \text{if } x \in [0, 1] \setminus \mathbb{Q} \end{cases}$$

Prove that $\lim_{x \to c} f(x) = 0$ for every $c \in [0, 1]$ and conclude that set of all points at which $f$ is discontinuous is precisely $[0, 1] \cap \mathbb{Q}$.

(b) Let $f : \mathbb{R} \to \mathbb{R}$ be bounded.

i. Recall that we defined the oscillation of $f$ at $x$ to be

$$\omega_f(x) := \lim_{\delta \to 0^+} \sup_{y, z \in B_\delta(x)} |f(y) - f(z)|.$$

Briefly explain why this is a well defined notion and prove that

$$f \text{ is continuous at } x \iff \omega_f(x) = 0.$$

ii. Prove that for every $\varepsilon > 0$ the set $A_\varepsilon = \{x \in \mathbb{R} : \omega_f(x) \geq \varepsilon\}$ is closed and deduce from this that the set of all points at which $f$ is discontinuous is an $F_\sigma$ set.

4. Let $\{x_n\}_{n=1}^{\infty}$ be any enumeration of a given countable set $X \subseteq \mathbb{R}$. For each $n \in \mathbb{N}$ define

$$f_n(x) = \begin{cases} 1 & \text{if } x > x_n \\ 0 & \text{if } x \leq x_n \end{cases}$$

Prove that

$$f(x) = \sum_{n=1}^{\infty} \frac{1}{n^2} f_n(x)$$

defines an increasing function $f$ on $\mathbb{R}$ that is continuous on $\mathbb{R} \setminus X$.

1

<!-- page 2 -->

5. Let $C([0, 1])$ denote the collection of all real-valued continuous functions with domain $[0, 1]$.

(a) Show that $d_\infty(f, g) = \sup_{x \in [0,1]} |f(x) - g(x)|$ defines a metric on $C([0,1])$ and that with the "uniform" metric $C([0,1])$ is in fact a complete metric space.
(b) Prove that the unit ball $\{f \in C([0,1]) : d_\infty(f, 0) \leq 1\}$ is closed and bounded, but not compact.
(c) ** Challenge: Can you show that $C([0,1])$ with the metric $d_\infty$ is not totally bounded.
A set is totally bounded if, for every $\varepsilon > 0$, it can be covered by finitely many balls of radius $\varepsilon$.

6. Let

$$g(x) = \sum_{n=0}^{\infty} \frac{1}{1 + n^2 x}.$$

(a) Show that the series defining $g$ does not converge uniformly on $(0, \infty)$, but none the less still defines a continuous function on $(0, \infty)$.

Hint for the first part: Show that if $\sum_{n=0}^{\infty} g_n(x)$ converges uniformly on a set $X$, then the sequence of functions $\{g_n\}$ must converge uniformly to 0 on $X$.

(b) Is $g$ differentiable on $(0, \infty)$? If so, is the derivative function $g'$ continuous on $(0, \infty)$?

7. Let $h_n(x) = \frac{x}{(1 + x)^{n+1}}$.

(a) Prove that $h_n$ converges uniformly to 0 on $[0, \infty)$.
(b) i. Verify that

$$\sum_{n=0}^{\infty} h_n(x) = \begin{cases} 1 & \text{if } x > 0 \\ 0 & \text{if } x = 0 \end{cases}$$

ii. Does $\sum_{n=0}^{\infty} h_n$ converge uniformly on $[0, \infty)$?

(c) Prove that $\sum_{n=0}^{\infty} h_n$ converges uniformly on $[a, \infty)$ for any $a > 0$.

### Extra Challenge Problems

Not to be handed in with the assignment

1. Given an arbitrary $F_\sigma$ set $V$, can you produce a function whose discontinuities lie precisely in $V$?

Hint: First try to do this for an arbitrary closed set.

2. (Baire Category Theorem) Prove that if $X$ is a non-empty complete metric space, then $X$ cannot be written as a countable union of nowhere dense sets.

Hint: Modify the proof given in class of the special case $X = \mathbb{R}$ replacing the use of the nested interval property with the following fact (which you should prove):

If $F_1 \supseteq F_2 \supseteq \cdots$ is a nested sequence of closed non-empty and bounded sets in a complete metric space $X$ with $\lim_{n \to \infty} \text{diam } F_n = 0$, then $\bigcap_{n=1}^{\infty} F_n$ contains exactly one point.

3. Complete the proof, sketched in class, of the so-called Lebesgue Criterion: A bounded function on an interval $[a, b]$ is Riemann integrable if and only if its set of discontinuities has measure zero.

(a) Prove that if the set of discontinuities of $f$ has measure zero, then $f$ is Riemann integrable.
[Hint: Let $\varepsilon > 0$. Cover the compact set $A_\varepsilon$ (defined in Q3(b)ii. above) by a finite number of open intervals whose total length is $\leq \varepsilon$. Select and appropriate partition of $[a, b]$ and estimate the difference between the upper and lower sums of $f$ over this partition.]
(b) Prove that if $f$ is Riemann integrable on $[a, b]$, then its set of discontinuities has measure zero.
[Hint: The set of discontinuities of $f$ is contained in $\bigcup_n A_{1/n}$. Given $\varepsilon > 0$, choose a partition $P$ such that $U(f, P) - L(f, P) < \varepsilon/n$. Show that the total length of the intervals in $P$ whose interiors intersect $A_{1/n}$ is $\leq \varepsilon$.]

2

<!-- page 3 -->

# Math 8100 Assignment 2

## Lebesgue measure and outer measure

Due date: Wednesday the 5th of September 2018

1. Prove that if $E \subseteq \mathbb{R}$ with $m_*(E) = 0$, then $E^2 := \{x^2 \mid x \in E\}$ also has Lebesgue outer measure zero.

Hint: First consider the case when $E$ is a bounded subset of $\mathbb{R}$.

[To what extent can you generalize this result?]

2. Prove that if $E_1$ and $E_2$ are measurable subsets of $\mathbb{R}^n$, then

$$m(E_1 \cup E_2) + m(E_1 \cap E_2) = m(E_1) + m(E_2).$$

3. Suppose that $A \subseteq E \subseteq B$, where $A$ and $B$ are Lebesgue measurable subsets on $\mathbb{R}^n$.

(a) Prove that if $m(A) = m(B) < \infty$, then $E$ is measurable.
(b) Give an example showing that the same conclusion does not hold if $A$ and $B$ have infinite measure.

4. Suppose $A$ and $B$ are a pair of compact subsets of $\mathbb{R}^n$ with $A \subseteq B$, and let $a = m(A)$ and $b = m(B)$. Prove that for any $c$ with $a < c < b$, there is a compact set $E$ with $A \subseteq E \subseteq B$ and $m(E) = c$.

Hint: As a warm-up example, consider the one dimensional example where $A$ a compact measurable subset of $B := [0, 1]$ and the quantity $m(A) + t - m(A \cap [0, t])$ as a function of $t$.

5. Let $\mathcal{N}$ denote the non-measurable subset of $[0, 1]$ that was constructed in lecture.

(a) Prove that if $E$ is a measurable subset of $\mathcal{N}$, then $m(E) = 0$.
(b) Show that $m_*([0, 1] \setminus \mathcal{N}) = 1$

[Hint: Argue by contradiction and pick an open set $G$ such that $[0, 1] \setminus \mathcal{N} \subseteq G \subseteq [0, 1]$ with $m_*(G) \leq 1 - \varepsilon$.]

(c) Conclude that there exists disjoint sets $E_1 \subseteq [0, 1]$ and $E_2 \subseteq [0, 1]$ for which

$$m_*(E_1 \cup E_2) \neq m_*(E_1) + m_*(E_2).$$

6. (a) The Borel-Cantelli Lemma. Suppose $\{E_j\}_{j=1}^\infty$ is a countable family of measurable subsets of $\mathbb{R}^n$ and that

$$\sum_{j=1}^\infty m(E_j) < \infty.$$

Let

$$E = \limsup_{j \to \infty} E_j := \{x \in \mathbb{R}^n : x \in E_j, \text{ for infinitely many } j\}.$$

Show that $E$ is measurable and that $m(E) = 0$. Hint: Write $E = \cap_{k=1}^\infty \cup_{j \geq k} E_j$.

(b) Given any irrational $x$ one can show (using the pigeonhole principle, for example) that there exists infinitely many fractions $a/q$, with $a$ and $q$ relatively prime integers, such that

$$\left| x - \frac{a}{q} \right| \leq \frac{1}{q^2}.$$

However, show that the set of those $x \in \mathbb{R}$ such that there exists infinitely many fractions $a/q$, with $a$ and $q$ relatively prime integers, such that

$$\left| x - \frac{a}{q} \right| \leq \frac{1}{q^3}$$

is a set of Lebesgue measure zero.

1

<!-- page 4 -->

# Extra Challenge Problems

Not to be handed in with the assignment

1. Prove that any $E \subset \mathbb{R}$ with $m_*(E) > 0$ necessarily contains a non-measurable set.

2. The outer Jordan content $J_*(E)$ of a set $E$ in $\mathbb{R}$ is defined by

$$J_*(E) = \inf \sum_{j=1}^{N} |I_j|,$$

where the infimum is taken over every finite covering $E \subseteq \cup_{j=1}^{N} I_j$, by intervals $I_j$.

(a) Prove that $J_*(E) = J_*(\bar{E})$ for every set $E$ (here $\bar{E}$ denotes the closure of $E$).
(b) Exhibit a countable subset $E \subseteq [0, 1]$ such that $J_*(E) = 1$ while $m_*(E) = 0$.

3. If $I$ is a bounded interval and $\alpha \in (0, 1)$, let us call the open interval with the same midpoint as $I$ and length equal to $\alpha$ times the length of $I$ the "open middle $\alpha$th" of $I$. If $\{\alpha_j\}_{j=1}^{\infty}$ is any sequence of numbers in $(0, 1)$, then, we can define a decreasing sequence $\{K_j\}$ of closed sets as follows: $K_0 = [0, 1]$, and $K_j$ is obtained by removing the open middle $\alpha_j$th from each of the intervals that make up $K_{j-1}$. The resulting limiting set $K = \bigcap_{j=1}^{\infty} K_j$ is called a generalized Cantor set.

(a) Suppose $\{\alpha_j\}_{j=1}^{\infty}$ is any sequence of numbers in $(0, 1)$.

i. Prove that $\prod_{j=1}^{\infty} (1 - \alpha_j) > 0$ if and only if $\sum_{j=1}^{\infty} \alpha_j < \infty$.
ii. Given $\beta \in (0, 1)$, exhibit a sequence $\{\alpha_j\}$ such that $\prod_{j=1}^{\infty} (1 - \alpha_j) = \beta$.

(b) Given $\beta \in (0, 1)$, construct an open set $G$ in $[0, 1]$ whose boundary has Lebesgue measure $\beta$.

Hint: Every closed nowhere dense set is the boundary of an open set.

2

<!-- page 5 -->

# Math 8100 Assignment 3

## Lebesgue measurable sets and functions

Due date: 5:00 pm Friday the 20th of September 2019

1. (a) Prove that for every $E \subseteq \mathbb{R}^n$ there exists a Borel set $B \supseteq E$ with the property that $m(B) = m_*(E)$.

- (b) Prove that if $E \subseteq \mathbb{R}^n$ is Lebesgue measurable, then there exists a Borel set $B \subseteq E$ with the property that $m(B) = m(E)$.
- (c) Prove that if $E \subseteq \mathbb{R}^n$ is Lebesgue measurable with $m(E) < \infty$, then for every $\varepsilon > 0$ there exists a set $A$ that is a finite union of closed cubes such that $m(E \triangle A) < \varepsilon$.

[Recall that $E \triangle A$ stands for the symmetric difference, defined by $E \triangle A = (E \setminus A) \cup (A \setminus E)$]

2. Let $E$ be a Lebesgue measurable subset of $\mathbb{R}^n$ with $m(E) > 0$ and $\varepsilon > 0$.

- (a) Prove that $E$ "almost" contains a closed cube in the sense that there exists a closed cube $Q$ such that $m(E \cap Q) \geq (1 - \varepsilon)m(Q)$.
- (b) Prove that the so-called difference set $E - E := \{d : d = x - y \text{ with } x, y \in E\}$ necessarily contains an open ball centered at the origin.

Hint: It may be useful to observe that $d \in E - E \Longleftrightarrow E \cap (E + d) \neq \emptyset$.

3. We say that a function $f : \mathbb{R}^n \to \mathbb{R}$ is upper semicontinuous at a point $x$ in $\mathbb{R}^n$ if

$$f(x) \geq \limsup_{y \to x} f(y).$$

Prove that if $f$ is upper semicontinuous at every point $x$ in $\mathbb{R}^n$, then $f$ is Borel measurable.

4. Let $\{f_n\}$ be a sequence of measurable functions on $\mathbb{R}^n$. Prove that $\{x \in \mathbb{R}^n : \lim_{n \to \infty} f_n(x) \text{ exists}\}$ defines a measurable set.
5. Recall that the Cantor set $\mathcal{C}$ is the set of all $x \in [0, 1]$ that have a ternary expansion $x = \sum_{k=1}^{\infty} a_k 3^{-k}$ with $a_k \neq 1$ for all $k$. Consider the function

$$f(x) = \sum_{k=1}^{\infty} b_k 2^{-k} \text{ where } b_k = a_k/2.$$

- (a) Show that $f$ is well defined and continuous on $\mathcal{C}$, and moreover $f(0) = 0$ as well as $f(1) = 1$.
- (b) Prove that there exists a continuous function that maps a measurable set to a non-measurable set.

6. Let us examine the map $f$ defined in Question 5 even more closely. One readily sees that if $x, y \in \mathcal{C}$ and $x < y$, then $f(x) < f(y)$ unless $x$ and $y$ are the two endpoints of one of the intervals removed from $[0, 1]$ to obtain $\mathcal{C}$. In this case $f(x) = \ell 2^m$ for some integers $\ell$ and $m$, and $f(x)$ and $f(y)$ are the two binary expansions of this number. We can therefore extend $f$ to a map $F : [0, 1] \to [0, 1]$ by declaring it to be constant on each interval missing from $\mathcal{C}$. $F$ is called the Cantor-Lebesgue function.

- (a) Prove that $F$ is non-decreasing and continuous.
- (b) Let $G(x) = F(x) + x$. Show that $G$ is a bijection from $[0, 1]$ to $[0, 2]$.
- (c) i. Show that $m(G(\mathcal{C})) = 1$.

ii. By considering rational translates of $\mathcal{N}$ (the non-measurable subset of $[0, 1]$ that we constructed in class), prove that $G(\mathcal{C})$ necessarily contains a (Lebesgue) non-measurable set $\mathcal{N}'$.

iii. Let $E = G^{-1}(\mathcal{N}')$. Show that $E$ is Lebesgue measurable, but not Borel.

(d) Give an example of a measurable function $\varphi$ such that $\varphi \circ G^{-1}$ is not measurable.

Hint: Let $\varphi$ be the characteristic function of a null set whose image under $G$ is not measurable.

1

<!-- page 6 -->

# Extra Challenge Problems

Not to be handed in with the assignment

1. Let $\chi_{[0,1]}$ be the characteristic function of $[0, 1]$. Show that there is no function $f$ satisfying $f = \chi_{[0,1]}$ almost everywhere which is also continuous on all of $\mathbb{R}$.
2. Question 6d above supplies us with an example that if $f$ and $g$ are Lebesgue measurable, then it does not necessarily follow that $f \circ g$ will be Lebesgue measurable, even if $g$ is assumed to be continuous. Prove that if $f$ is Borel measurable, then $f \circ g$ will be Lebesgue or Borel measurable whenever $g$ is.
3. Let $f$ be a measurable function on $[0, 1]$ with $|f(x)| < \infty$ for a.e. $x$. Prove that there exists a sequence of continuous functions $\{g_n\}$ on $[0, 1]$ such that $g_n \to f$ for a.e. $x \in [0, 1]$.

2

<!-- page 7 -->

# Math 8100 Assignment 4
## Lebesgue Integration

Due date: Tuesday the 1st of October 2019

Definition. Let $E$ be a Lebesgue measurable subset of $\mathbb{R}^n$.

We say that a measurable function $f : E \to \mathbb{C}$ is integrable on $E$ if $\int_E |f(x)| \, dx < \infty$.

1. (a) Give an example of a continuous integrable function $f$ on $\mathbb{R}$ for which $f(x) \twoheadrightarrow 0$ as $|x| \to \infty$.

(b) Prove that if $f$ is integrable on $\mathbb{R}$ and uniformly continuous, then $\lim_{|x| \to \infty} f(x) = 0$.

2. Let $f$ be an integrable function on $\mathbb{R}^n$.

(a) Prove that $\{x : |f(x)| = \infty\}$ has measure equal to zero.

(b) Let $\varepsilon > 0$. Prove that there exists a measurable set $E$ with $m(E) < \infty$ for which

$$\int_E |f| > \left( \int |f| \right) - \varepsilon.$$

3. Let $f$ be a function in $L^+(\mathbb{R}^n)$ that is finite almost everywhere.

Let $E_{2^k} = \{x : f(x) > 2^k\}$, $F_k = \{x : 2^k < f(x) \le 2^{k+1}\}$, and note that since $f$ is finite almost everywhere it follows that $\bigcup_{k=-\infty}^{\infty} F_k = \{x : f(x) > 0\}$, and the sets $F_k$ are disjoint. Prove that

$$\int f(x) < \infty \iff \sum_{k=-\infty}^{\infty} 2^k m(F_k) < \infty \iff \sum_{k=-\infty}^{\infty} 2^k m(E_{2^k}) < \infty.$$

4. Prove the following:

(a)

$$\int_{\{x \in \mathbb{R}^n : |x| \le 1\}} |x|^{-p} \, dx < \infty \quad \text{if and only if} \quad p < n.$$

(b)

$$\int_{\{x \in \mathbb{R}^n : |x| \ge 1\}} |x|^{-p} \, dx < \infty \quad \text{if and only if} \quad p > n.$$

Hint: One possible approach is to use the first equivalence in Question 3 above. I suggest however that in this case you also try simply writing $\mathbb{R}^n$ as a disjoint union of the annuli $A_k = \{2^k < |x| \le 2^{k+1}\}$.

5. Given any integrable function $f$ on $\mathbb{R}^n$, the Fourier transform of $f$ is defined by

$$\widehat{f}(\xi) = \int_{\mathbb{R}^n} f(x) e^{-2\pi i x \cdot \xi} \, dx$$

where $x \cdot \xi = x_1 \xi_1 + \cdots + x_n \xi_n$. Show that $\widehat{f}$ is a bounded continuous function of $\xi$.

6. Let $\{f_k\}$ be a sequence of integrable functions on $\mathbb{R}^n$, $f$ be integrable on $\mathbb{R}^n$, and $\lim_{k \to \infty} f_k = f$ a.e.

(a) Suppose further that

$$\lim_{k \to \infty} \int |f_k(x)| \, dx = A < \infty \quad \text{and} \quad \int |f(x)| \, dx = B.$$

1

<!-- page 8 -->

i. Prove that

$$\lim _ {k \rightarrow \infty} \int | f _ {k} (x) - f (x) | d x = A - B.$$

Hint: Use the fact that

$$| f _ {k} (x) | - | f (x) | \leq | f _ {k} (x) - f (x) | \leq | f _ {k} (x) | + | f (x) |.$$

ii. Give an example of a sequence $\{f_k\}$ of such functions for which $A \neq B$.

(b) Deduce that

$$\int | f - f _ {k} | \rightarrow 0 \quad \Longleftrightarrow \quad \int | f _ {k} | \rightarrow \int | f |.$$

7. (a) Suppose that $f(x)$ and $xf(x)$ are both integrable functions on $\mathbb{R}$. Prove that the function

$$F (t) = \int_ {\mathbb {R}} f (x) \cos (t x) d x.$$

is differentiable at every $t$ and find a formula for $F'(t)$.

(b) Giving complete justification, evaluate

$$\lim _ {t \rightarrow 0} \int_ {0} ^ {1} \frac {e ^ {t \sqrt {x}} - 1}{t} d x.$$

### Extra Challenge Problems

Not to be handed in with the assignment

1. Assume Fatou's theorem and deduce the monotone convergence theorem from it.

2. A sequence $\{f_k\}$ of integrable functions on $\mathbb{R}^n$ is said to converge in measure to $f$ if for every $\varepsilon > 0$,

$$\lim _ {k \rightarrow \infty} m (\{x \in \mathbb {R} ^ {n}: | f _ {k} (x) - f (x) | \geq \varepsilon \}) = 0.$$

- (a) Prove that if $f_k \to f$ in $L^1$ then $f_k \to f$ in measure.
- (b) Give an example to show that the converse of Question 2a is false.
- (c) Prove that if we make the additional assumption that there exists an integrable function $g$ such that $|f_k| \leq g$ for all $k$, then $f_k \to f$ in measure implies that

i. * (Bonus points) $f \in L^1$

Hint: First show that $\{f_k\}$ contains a subsequence which converges to $f$ almost everywhere.

ii. $f_k \to f$ in $L^1$.

Hint: Try using absolute continuity and "small tails property" of the Lebesgue integral.

3. Let $\Omega \subseteq \mathbb{R}^n$ be measurable with $m(\Omega) < \infty$. A set $\Phi \subseteq L^1(\Omega)$ is said to be uniformly integrable if, for any $\varepsilon > 0$ there exists $\delta > 0$ such that whenever $f \in \Phi$ and $E \subseteq \Omega$ is measurable with $m(E) < \delta$, then

$$\int_ {E} | f (x) | d x < \varepsilon.$$

- (a) Prove that if $f \in L^1(\Omega)$ and $\{f_k\}$ is a uniformly integrable sequence of functions in $L^1(\Omega)$ such that $f_k \to f$ almost everywhere on $\Omega$, then $f_k \to f$ in $L^1(\Omega)$.
- (b) Is it necessary to assume that $f \in L^1(\Omega)$?

2

<!-- page 9 -->

# Math 8100 Assignment 5
Repeated Integration

Due date: Friday the 18th of October 2019

1. Prove that if $\{a_{jk}\}_{(j,k)\in\mathbb{N}\times\mathbb{N}}$ is a "double sequence" with $a_{jk} \ge 0$ for all $(j,k) \in \mathbb{N} \times \mathbb{N}$, then

$$\sum_{j=1}^{\infty} \sum_{k=1}^{\infty} a_{jk} = \sup \left\{ \sum_{(j,k)\in B} a_{jk} : B \text{ is a finite subset of } \mathbb{N} \times \mathbb{N} \right\}$$

and deduce from this that

$$\sum_{j=1}^{\infty} \sum_{k=1}^{\infty} a_{jk} = \sum_{k=1}^{\infty} \sum_{j=1}^{\infty} a_{jk}.$$

This conclusion holds more generally provided $\sum_{j=1}^{\infty} \sum_{k=1}^{\infty} |a_{jk}| < \infty$, see Theorem 8.3 in "Baby Rudin".

2. Let $f \in L^1([0, 1])$, and for each $x \in [0, 1]$ define

$$g(x) = \int_x^1 \frac{f(t)}{t} \, dt.$$

Show that $g \in L^1([0, 1])$ and that

$$\int_0^1 g(x) \, dx = \int_0^1 f(x) \, dx.$$

3. Carefully prove that if we define

$$f(x, y) := \begin{cases} \frac{x^{1/3}}{(1 + xy)^{3/2}} & \text{if } 0 \le x \le y \\ 0 & \text{otherwise} \end{cases}$$

for each $(x, y) \in \mathbb{R}^2$, then $f$ defines a function in $L^1(\mathbb{R}^2)$.

4. Let $A, B \subseteq \mathbb{R}^n$ be bounded measurable sets with positive Lebesgue measure. For each $t \in \mathbb{R}^n$ define the function

$$g(t) = m(A \cap (t - B))$$

where $t - B = \{t - b : b \in B\}$.

(a) Prove that $g$ is a continuous function and

$$\int_{\mathbb{R}^n} g(t) \, dt = m(A) m(B).$$

(b) Conclude that the sumset

$$A + B = \{a + b : a \in A \text{ and } b \in B\}$$

contains a non-empty open subset of $\mathbb{R}^n$.

5. Let $f, g \in L^1([0, 1])$ and for each $0 \le x \le 1$ define

$$F(x) := \int_0^x f(y) \, dy \quad \text{and} \quad G(x) := \int_0^x g(y) \, dy.$$

Prove that

$$\int_0^1 F(x)g(x) \, dx = F(1)G(1) - \int_0^1 f(x)G(x) \, dx.$$

1

<!-- page 10 -->

6. Let $f \in L^1(\mathbb{R})$. For any $h > 0$ we define

$$A_h(f)(x) := \frac{1}{2h} \int_{x-h}^{x+h} f(y) \, dy$$

(a) Prove that for all $h > 0$,

$$\int_{\mathbb{R}} |A_h(f)(x)| \, dx \le \int_{\mathbb{R}} |f(x)| \, dx.$$

(b) Prove that

$$\lim_{h \to 0^+} \int_{\mathbb{R}} |A_h(f)(x) - f(x)| \, dx = 0.$$

One can in fact show that $\lim_{h \to 0^+} A_h(f) = f$ almost everywhere. This result is actually equivalent to the Lebesgue Density Theorem in $\mathbb{R}$ and we will establish this later in the course.

### Extra Challenge Problems

Not to be handed in with the assignment

1. (a) Prove that

$$\int_0^\infty \left| \frac{\sin x}{x} \right| \, dx = \infty.$$

(b) By considering the iterated integral

$$\int_0^\infty \left( \int_0^\infty x e^{-xy} (1 - \cos y) \, dy \right) \, dx$$

show (with justification) that

$$\lim_{A \to \infty} \int_0^A \frac{\sin x}{x} \, dx = \frac{\pi}{2}.$$

2. Suppose that $F$ is a closed subset of $\mathbb{R}$ whose complement has finite measure. Let $\delta(x)$ denote the distance from $x$ to $F$, namely

$$\delta(x) = d(x, F) = \inf\{|x - y| : y \in F\}$$

and

$$I_F(x) = \int_{-\infty}^\infty \frac{\delta(y)}{|x - y|^2} \, dy.$$

- (a) Prove that $\delta$ is continuous, by showing that it satisfies the Lipschitz condition $|\delta(x) - \delta(y)| \le |x - y|$.
- (b) Show that $I_F(x) = \infty$ if $x \notin F$.
- (c) Show that $I_F(x) < \infty$ for a.e. $x \in F$, by showing that $\int_F I_F(x) \, dx < \infty$.

2

<!-- page 11 -->

# Math 8100 Assignment 6

## The Fourier Transform

Due date: Thursday the 31st of October 2019

Recall that we have defined the Fourier transform of an integrable function $f$ on $\mathbb{R}^n$ by

$$\widehat{f}(\xi) = \int_{\mathbb{R}^n} f(x) e^{-2\pi i x \cdot \xi} \, dx$$

where $x \cdot \xi = x_1 \xi_1 + \cdots + x_n \xi_n$ and the convolution of two integrable functions $f$ and $g$ on $\mathbb{R}^n$ by

$$f * g(x) = \int_{\mathbb{R}^n} f(x - y) g(y) \, dy.$$

1. Prove that if $f \in L^1(\mathbb{R}^n)$, then $\widehat{f}(\xi) \to 0$ as $|\xi| \to \infty$. (This is called the Riemann-Lebesgue lemma.)

Hint: Write $\widehat{f}(\xi) = \frac{1}{2} \int [f(x) - f(x - \xi')] e^{-2\pi i x \cdot \xi} \, dx$, where $\xi' = \frac{\xi}{2|\xi|^2}$.

2. (a) Prove that if $f, g \in L^1(\mathbb{R}^n)$, then $\widehat{f * g}(\xi) = \widehat{f}(\xi) \widehat{g}(\xi)$ for all $\xi \in \mathbb{R}^n$.

(b) Conclude from part (a) that

i. if $f, g, h \in L^1(\mathbb{R}^n)$, then $f * g = g * f$ and $(f * g) * h = f * (g * h)$ almost everywhere.

ii. there does not exist $I \in L^1(\mathbb{R}^n)$ such that $f * I = f$ almost everywhere for all $f \in L^1(\mathbb{R}^n)$.

3. Let $f \in L^1(\mathbb{R}^n)$.

(a) Show that if $y \in \mathbb{R}^n$ and

i. $g(x) = f(x - y)$ for all $x \in \mathbb{R}^n$, then $\widehat{g}(\xi) = e^{-2\pi i y \cdot \xi} \widehat{f}(\xi)$ for all $\xi \in \mathbb{R}^n$.

ii. $h(x) = e^{2\pi i x \cdot y} f(x)$ for all $x \in \mathbb{R}^n$, then $\widehat{h}(\xi) = \widehat{f}(\xi - y)$ for all $\xi \in \mathbb{R}^n$.

(b) Show that if $T$ be a non-singular linear transformation of $\mathbb{R}^n$ and $S = (T^*)^{-1}$ denote its inverse transpose, then

$$\widehat{f \circ T}(\xi) = \frac{1}{|\det T|} \widehat{f}(S\xi)$$

for all $\xi \in \mathbb{R}^n$.

4. (a) Let $f \in L^1(\mathbb{R})$.

i. Let $g(x) = x f(x)$. Show that if $g \in L^1$, then $\widehat{f}$ is differentiable and $\frac{d}{d\xi} \widehat{f}(\xi) = -2\pi i \widehat{g}(\xi)$.

ii. Let $f \in C_0^1(\mathbb{R})$ and $h(x) = \frac{d}{dx} f(x)$. Show that if $h \in L^1$, then $\widehat{h}(\xi) = 2\pi i \xi \widehat{f}(\xi)$.

Recall that $C_0^1(\mathbb{R})$ is the collection of functions in $C^1(\mathbb{R})$ which vanishes at infinity.

(b) Let $G(x) = e^{-\pi x^2}$. By considering the derivative of $\widehat{G}(\xi)/G(\xi)$, show that $\widehat{G}(\xi) = G(\xi)$.

Hint: You may also want to use the fact that $\int_{\mathbb{R}} G(x) \, dx = 1$ (see "challenge" problem).

5. The functions $D$, $F$, and $P$ defined below are all bounded $L^+(\mathbb{R})$ functions with integrals equal to 1.

(a) Show that if

$$D(x) = \begin{cases} 1 & \text{if } |x| \le 1/2 \\ 0 & \text{otherwise} \end{cases}$$

then

$$\widehat{D}(\xi) = \frac{\sin \pi \xi}{\pi \xi}.$$

This gives, in light of Assignment 5 Challenge Problem 1(a), an explicit example of a function which is not in $L^1(\mathbb{R})$, but yet is the Fourier transform of an $L^1$ function. See Question 6 for additional higher dimensional examples.

1

<!-- page 12 -->

(b) Let

$$F ( x ) = \left\{ \begin{array} { l l } { 1 - | x | } & { { \mathrm { i f ~ } } | x | \leq 1 } \\ { 0 } & { { \mathrm { o t h e r w i s e } } } \end{array} \right. .$$

i. Show that

$$\widehat { F } ( \xi ) = \left( \frac { \sin \pi \xi } { \pi \xi } \right) ^ { 2 } .$$

Hint: It may help to write $\widehat { F } ( \xi ) = h ( \xi ) + h ( - \xi )$ where $h ( \xi ) = e ^ { 2 \pi i \xi } \int _ { 0 } ^ { 1 } y e ^ { - 2 \pi i y \xi } d y$.

ii. Find the Fourier transform of the function

$$f ( x ) = \left( \frac { \sin \pi x } { \pi x } \right) ^ { 2 } .$$

Be careful to fully justify your answer.

(c) Show that if

$$P ( x ) = { \frac { 1 } { \pi } } { \frac { 1 } { 1 + x ^ { 2 } } } .$$

then

$$\int _ { - \infty } ^ { \infty } e ^ { - 2 \pi | \xi | } e ^ { 2 \pi i x \xi } d \xi = P ( x )$$

and hence that

$$\widehat { P } ( \xi ) = e ^ { - 2 \pi | \xi | } .$$

Be careful to fully justify your answer.

Remark: In Questions 4b and 5 above D is for Dirichlet, F is for Fejér, P is for Poisson, and G is for Gauss-Weierstrass. The respective "approximate identities", namely $\{ ( \widehat { D } ) _ { t } \} _ { t > 0 }$, $\{ ( \widehat { F } ) _ { t } \} _ { t > 0 }$, $\{ P _ { t } \} _ { t > 0 }$, and $\{ G _ { \sqrt { t } } \} _ { t > 0 }$, are generally referred to as Dirichlet, Fejér, Poisson, and Gauss-Weierstrass kernels.

6. Show that for any $\varepsilon > 0$ the function $F ( \xi ) = ( 1 + | \xi | ^ { 2 } ) ^ { - \varepsilon }$ is the Fourier transform of an $L ^ { 1 } ( \mathbb { R } ^ { n } )$ function.

Hint: Consider the function

$$f ( x ) = \int _ { 0 } ^ { \infty } G _ { t } ( x ) e ^ { - \pi t ^ { 2 } } t ^ { 2 \varepsilon - 1 } d t ,$$

where $G _ { t } ( x ) = t ^ { - n } e ^ { - \pi | x | ^ { 2 } / t ^ { 2 } }$. Now use Fubini/Tonelli to prove that $f \in L ^ { 1 } ( \mathbb { R } ^ { n } )$ with $\widehat { f } ( \xi ) = F ( \xi ) \| f \| _ { 1 }$.

### Extra Challenge Problems

Not to be handed in with the assignment

1. By considering the iterated integral

$$\int _ { 0 } ^ { \infty } \left( \int _ { 0 } ^ { \infty } x e ^ { - x ^ { 2 } ( 1 + y ^ { 2 } ) } d x \right) d y$$

show (with justification) that

$$\int _ { 0 } ^ { \infty } e ^ { - x ^ { 2 } } d x = { \frac { \sqrt { \pi } } { 2 } }$$

and hence that

$$\int _ { - \infty } ^ { \infty } e ^ { - \pi x ^ { 2 } } d x = 1 .$$

2

<!-- page 13 -->

# Math 8100 Assignment 7
Hilbert Spaces

Due date: Thursday 14th of November 2019

1. (a) Prove that \(\ell^2 (\mathbb{N})\) is complete.

Recall that \(\ell^2 (\mathbb{N}):= \{x = \{x_j\}_{j = 1}^\infty :\| x\|_{\ell^2} <   \infty \}\) , where \(\| x\|_{\ell^2}:= \left(\sum_{j = 1}^{\infty}|x_j|^2\right)^{1 / 2}\)

(b) Let \( H \) be a Hilbert space. Prove the so-called polarization identity, namely that for any \( x, y \in H \),

\[
\langle x, y \rangle = \frac {1}{4} \left(\| x + y \| ^ {2} - \| x - y \| ^ {2} + i \| x + i y \| ^ {2} - i \| x - i y \| ^ {2}\right)
\]

and conclude that any invertible linear map from \(H\) to \(\ell^2 (\mathbb{N})\) is unitary if and only if it is isometric.

Recall that if  \( H_{1} \)  and  \( H_{2} \)  are Hilbert spaces with inner products  \( \langle\cdot,\cdot\rangle_{1} \)  and  \( \langle\cdot,\cdot\rangle_{2} \) , then a mapping  \( U:H_{1}\to H_{2} \)  is said to be unitary if it is an invertible linear map that preserves inner products, namely  \( \langle Ux,Uy\rangle_{2}=\langle x,y\rangle_{1} \) , and an isometry if it preserves “lengths”, namely  \( \|Ux\|_{2}=\|x\|_{1} \) .

2. Let \(E\) be a subset of a Hilbert space \(H\).

(a) Show that \( E^{\perp} := \{x \in H : \langle x, y \rangle = 0 \text{ for all } y \in E\} \) is a closed subspace of \( H \).
(b) Show that \((E^{\perp})^{\perp}\) is the smallest closed subspace of \(H\) that contains \(E\).

3. In \( L^2([0,1]) \) let \( e_0(x) = 1 \), \( e_1(x) = \sqrt{3}(2x - 1) \) for all \( x \in (0,1) \).

(a) Show that \( e_0, e_1 \) is an orthonormal system in \( L^2(0,1) \).
(b) Show that the polynomial of degree 1 which is closest with respect to the norm of \( L^2(0,1) \) to the function \( f(x) = x^2 \) is given by \( g(x) = x - 1/6 \). What is \( \| f - g \|_2 \)?

4. (a) Verify that the following systems are orthogonal in \( L^2([0,1]) \):

i. \(\{1 / \sqrt{2},\cos (2\pi x),\sin (2\pi x),\dots ,\cos (2\pi kx),\sin (2\pi kx),\ldots \}\)
ii. \(\{e^{2\pi ikx}\}_{k = -\infty}^{\infty}\)

(b) Let \( f \in L^{1}([0,1]) \).

i. Show that for any \(\epsilon > 0\) we can write \(f = g + h\), where \(g \in L^2\) and \(\|h\|_1 < \epsilon\).
ii. Use this decomposition of \( f \) to prove the so-called Riemann-Lebesgue lemma:

\[
\lim _ {k \rightarrow \infty} \int_ {0} ^ {1} f (x) \cos (2 \pi k x) d x = \lim _ {k \rightarrow \infty} \int_ {0} ^ {1} f (x) \sin (2 \pi k x) d x = 0
\]

5. (a) The first three Legendre polynomials are

\[
P _ {0} (x) = 1, \quad P _ {1} (x) = x, \quad P _ {2} (x) = (3 x ^ {2} - 1) / 2.
\]

Show that the orthonormal system in \( L^2([-1, 1]) \) obtained by applying the Gram-Schmidt process to \( 1, x, x^2 \) are scalar multiples of these.

1

<!-- page 14 -->

(b) Compute

$$\min_{a,b,c} \int_{-1}^{1} |x^3 - a - bx - cx^2|^2 \, dx$$

(c) Find

$$\max \int_{-1}^{1} x^3 g(x) \, dx$$

where $g$ is subject to the restrictions

$$\int_{-1}^{1} g(x) \, dx = \int_{-1}^{1} x g(x) \, dx = \int_{-1}^{1} x^2 g(x) \, dx = 0; \quad \int_{-1}^{1} |g(x)|^2 \, dx = 1.$$

6. Let

$$\mathcal{C} = \left\{ f \in L^2([0, 1]) : \int_{0}^{1} f(x) \, dx = 1 \text{ and } \int_{0}^{1} x f(x) \, dx = 2 \right\}$$

(a) Let $g(x) = 18x^2 - 5$. Show that $g \in \mathcal{C}$ and that

$$\mathcal{C} = g + \mathcal{S}^\perp$$

where $\mathcal{S}^\perp$ denotes the orthogonal complement of $\mathcal{S} = \text{Span}(\{1, x\})$.

(b) Find the function $f_0 \in \mathcal{C}$ for which

$$\int_{0}^{1} |f_0(x)|^2 \, dx = \inf_{f \in \mathcal{C}} \int_{0}^{1} |f(x)|^2 \, dx.$$

### Extra Challenge Problems

Not to be handed in with the assignment

1. Prove that every closed convex set $K$ in a Hilbert space has a unique element of minimal norm.
2. The Mean Ergodic Theorem: Let $U$ be a unitary operator on a Hilbert space $H$.

Prove that if $M = \{x : Ux = x\}$ and $S_N = \frac{1}{N} \sum_{n=0}^{N-1} U^n$, then $\lim_{N \to \infty} \|S_N x - Px\| = 0$ for all $x \in H$, where $Px$ denotes the orthogonal projection of $x$ onto $M$.

2

<!-- page 15 -->

# Math 8100 Assignment 8
## Basic Function Spaces

Due date: Tuesday the 26th of November 2019

1. Prove the following basic properties of $L^{\infty} = L^{\infty}(X)$, where $X$ is a measurable subset of $\mathbb{R}^n$:

- (a) $\| \cdot \|_{\infty}$ is a norm on $L^{\infty}$ and when equipped with this norm $L^{\infty}$ is a Banach space.
- (b) $\| f_n - f \|_{\infty} \to 0$ iff there exists $E \in \mathbb{R}^n$ such that $m(E^c) = 0$ and $f_n \to f$ uniformly on $E$.
- (c) Simple functions are dense in $L^{\infty}$, but continuous functions with compact support are not.

Recall that if $X \subseteq \mathbb{R}^n$ is measurable and $f$ is a measurable function on $X$, then we define

$$\| f \|_{\infty} = \inf \{ a \geq 0 : m(\{ x \in X : |f(x)| > a \}) = 0 \},$$

with the convention that $\inf \emptyset = \infty$, and

$$L^{\infty} = L^{\infty}(X) = \{ f : X \to \mathbb{C} \text{ measurable} : \| f \|_{\infty} < \infty \},$$

with the usual convention that two functions that are equal a.e. define the same element of $L^{\infty}$. Thus $f \in L^{\infty}$ if and only if there is a bounded function $g$ such that $f = g$ almost everywhere; we can take $g = f_{\chi_E}$ where $E = \{ x : |f(x)| \leq \| f \|_{\infty} \}$.

2. Let $X \subseteq \mathbb{R}^n$ be measurable.

(a) i. Prove that if $m(X) < \infty$, then

$$L^{\infty}(X) \subset L^2(X) \subset L^1(X) \tag{1}$$

with strict inclusion in each case, and that for any measurable $f : X \to \mathbb{C}$ one in fact has

$$\| f \|_{L^1(X)} \leq m(X)^{1/2} \| f \|_{L^2(X)} \leq m(X) \| f \|_{L^{\infty}(X)}.$$

ii. Give examples to show that no such result of the form (1) can hold if one drops the assumption that $m(x) < \infty$. Prove, furthermore, that if $L^2(X) \subseteq L^1(X)$, then $m(X) < \infty$.

(b) Prove that

$$\underbrace{L^1(X) \cap L^{\infty}(X) \subset L^2(X)}_{(\star)} \subset L^1(X) + L^{\infty}(X)$$

and that in addition to $(\star)$ one in fact has

$$\| f \|_{L^2(X)} \leq \| f \|_{L^1(X)}^{1/2} \| f \|_{L^{\infty}(X)}^{1/2}$$

for any measurable function $f : X \to \mathbb{C}$.

3. Prove that

$$\ell^1(\mathbb{Z}) \subset \ell^2(\mathbb{Z}) \subset \ell^{\infty}(\mathbb{Z})$$

with strict inclusion in each case, and that for any sequence $a = \{ a_j \}_{j \in \mathbb{Z}}$ of complex numbers one in fact has

$$\| a \|_{\ell^{\infty}(\mathbb{Z})} \leq \| a \|_{\ell^2(\mathbb{Z})} \leq \| a \|_{\ell^1(\mathbb{Z})}.$$

Recall that for $p = 1, 2, \infty$ we define

$$\ell^p(\mathbb{Z}) = \{ a = \{ a_j \}_{j \in \mathbb{Z}} \subseteq \mathbb{C} : \| a \|_{\ell^p(\mathbb{Z})} < \infty \}$$

where

$$\| a \|_{\ell^1(\mathbb{Z})} = \sum_{j=-\infty}^{\infty} |a_j|, \quad \| a \|_{\ell^2(\mathbb{Z})} = \left( \sum_{j=-\infty}^{\infty} |a_j|^2 \right)^{1/2}, \text{ and } \| a \|_{\ell^{\infty}(\mathbb{Z})} = \sup_j |a_j|.$$

1

<!-- page 16 -->

4. Let $C([0, 1])$ denote the space of all continuous real-valued functions on $[0, 1]$.

(a) Prove that $C([0, 1])$ is complete under the uniform norm $\|f\|_u := \sup_{x \in [0, 1]} |f(x)|$.
(b) Prove that $C([0, 1])$ is not complete under the $L^1$-norm $\|f\|_1 = \int_0^1 |f(x)| \, dx$

5. Let $H$ be a Hilbert space with orthonormal basis $\{u_n\}_{n=1}^\infty$.

(a) Let $\{a_n\}_{n=1}^\infty$ be a sequence of complex numbers. Prove that

$$\sum_{n=1}^\infty a_n u_n \text{ converges in } H \iff \sum_{n=1}^\infty |a_n|^2 < \infty,$$

and moreover that if $\sum_{n=1}^\infty |a_n|^2 < \infty$, then $\left\| \sum_{n=1}^\infty a_n u_n \right\| = \left( \sum_{n=1}^\infty |a_n|^2 \right)^{1/2}$.

(b) i. Is there a continuous linear functional $L$ on $H$ such that $L(u_n) = n^{-1}$ for all $n \in \mathbb{N}$? If $L$ exists, find its norm.
ii. Is there a continuous linear functional $L$ on $H$ such that $L(u_n) = n^{-1/2}$ for all $n \in \mathbb{N}$? If $L$ exists, find its norm.

6. For each $1 \le p \le \infty$, define $\Lambda_p : L^p([0, 1]) \to \mathbb{R}$ by

$$\Lambda_p(f) = \int_0^1 x^2 f(x) \, dx.$$

Explain why $\Lambda_p$ is a continuous linear functional and compute its norm (in terms of $p$).

# Extra Practice Problems

Not to be handed in with the assignment

1. Let $f$ and $g$ be two non-negative Lebesgue measurable functions on $[0, \infty)$. Suppose that

$$A := \int_0^\infty f(y) \, y^{-1/2} dy < \infty \quad \text{and} \quad B := \left( \int_0^\infty |g(y)|^2 dy \right)^{1/2} < \infty$$

Prove that

$$\int_0^\infty \left( \int_0^x f(y) \, dy \right) \frac{g(x)}{x} \, dx \le AB$$

2. Let $\{f_k\}$ be any sequence of functions in $L^2([0, 1])$ satisfying $\|f_k\|_2 \le 1$ for all $k \in \mathbb{N}$.

(a) i. Prove that if $f_k \to f$ either a.e. on $[0, 1]$ or in $L^1([0, 1])$, then $f \in L^2([0, 1])$ with $\|f\|_2 \le 1$. ii. Do either of the above hypotheses guarantee that $f_k \to f$ in $L^2([0, 1])$?
(b) Prove that if $f_k \to f$ a.e. on $[0, 1]$, then this in fact implies that $f_k \to f$ in $L^1([0, 1])$.

3. Let $1 \le p \le \infty$. Prove that if $\{f_k\}_{k=1}^\infty$ is a sequence of functions in $L^p(\mathbb{R}^n)$ with the property that

$$\sum_{k=1}^\infty \|f_k\|_p < \infty,$$

then $\sum f_k$ converges almost everywhere to an $L^p(\mathbb{R}^n)$ function with

$$\left\| \sum_{k=1}^\infty f_k \right\|_p \le \sum_{k=1}^\infty \|f_k\|_p.$$

2
