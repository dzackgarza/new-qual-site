<!-- page 1 -->

Zack Garza

①a

Note that if x ∈ C is an endpoint of a removed

interval, then x = k/3ⁿ for some integers

n ≥ 1 and 0 ≤ k ≤ 3ⁿ. So we just need a

real number x ∈ (0, 1) satisfying

a) x has some ternary expansion

x = Σᵢ₌₁^∞ aᵢ 3⁻ⁱ where aᵢ ≠ 1 for any i, and

b) x ≠ k/3ⁿ for any k, n ∈ ℕˣ⁰,

then we will have x ∈ C by (a) and x not an

endpoint by (b).

Claim: x = (0.02)₃ = (0.020202...)₃ works.

Base 3

Pf: By construction, x satisfies

(a) x = Σᵢ₌₀^∞ aᵢ 3⁻ⁱ, aᵢ ∈ {0, 2}

<!-- page 2 -->

So no $a_i = 1$ and thus $x \in C$.

(b) To see that $x$ satisfies (b), we can compute

$$\begin{array}{l} x = (0.020202 \dots) _ {3} \\ = 0.3 ^ {- 1} + 2.3 ^ {- 2} + 0.3 ^ {- 3} + 2.3 ^ {- 4} + \dots \\ = \sum_ {i = 1} ^ {\infty} 2.3 ^ {- 2 i} = 2 \sum_ {i = 1} ^ {\infty} 3 ^ {- 2 i} = 2 \sum_ {i = 1} ^ {\infty} \left(\frac {1}{a}\right) ^ {i} \\ = 2 \left(- 1 + \sum_ {i = 0} ^ {\infty} \left(\frac {1}{a}\right) ^ {i}\right) \\ = 2 \left(- 1 + \frac {1}{1 - \frac {1}{a}}\right) = 1 / 4, \\ \end{array}$$

where $4 \neq 3^{n}$ for any integer $n$. $\square$

①b If a set $X$ is nowhere dense in a topological

space, it equivalently satisfies

$$(\overline {X}) ^ {0} = \emptyset$$

(i.e, the interior of the closure is empty.)

<!-- page 3 -->

It then suffices to show that

a) C is closed, so $\overline{C} = C$, and
b) C has no interior points, so $C^0 = \emptyset$.

(a) To see that C is closed, we will show $C^c := [0,1] \setminus C$

is open. An arbitrary union of open sets is open,

so the claim is that $C^c = \bigcup_{j \in J} A_j$ for some

collection of open sets $\{A_j\}_{j \in J}$.

Consider $C_n$, the $n^{th}$ stage of the process used

to construct the Cantor set, so $C = \bigcap_{n=1}^{\infty} C_n$.

But by induction, $C_n^c$ is a union of open sets.

In particular, $C_1^c = (\frac{1}{3}, \frac{2}{3})$, and

$$C_n^c = \left( \bigcup_{i=1}^{n-1} C_i^c \right) \cup \left( \begin{array}{c} \text{Exactly } n \text{ open intervals} \\ \text{that were deleted} \end{array} \right),$$

Open by hypothesis open by construction

<!-- page 4 -->

So $C_n^c$ is open for each $n$. But then

$$C^c = (\bigcap_{n=1}^{\infty} C_n)^c = \bigcup_{i=1}^{\infty} C_n^c$$

is a union of open sets and thus open. So $C$ is closed.

(b) To see that $C^0 = \emptyset$, suppose towards a contradiction

that $x \in C^0$, so there exists some $\varepsilon > 0$ such that

$N_\varepsilon(x) := (x - \varepsilon, x + \varepsilon) \leqslant C$. Letting $\mu(I)$ denote the

length of an interval, we have $\mu(N_\varepsilon(x)) = 2\varepsilon > 0$.

Claim: Let $L_n := \mu(C_n)$, then $L_n = (\frac{2}{3})^n$.

This follows immediately by noting that $L_n$

satisfies the recurrence relation

$$L_{n+1} = \frac{2}{3} L_n, \quad L_0 = 1$$

Since an interval of length $\frac{1}{3} L_{n-1}$ is removed

at the $n^{th}$ stage, which has the unique claimed solution.

<!-- page 5 -->

But if $I_1 \subseteq I_2$ are real intervals, we must have
$$
\mu(I_1) \subseteq \mu(I_2), \text{ whereas if we choose } n \text{ large
}$
$$
\text{enough such that } (\frac{2}{3})^n < 2\varepsilon, \text{ we have}
$$
$$
(x - \varepsilon, x + \varepsilon) \subsetneq C = \bigcap_{i=1}^{\infty} C_i \Rightarrow (x - \varepsilon, x + \varepsilon) \subseteq C_n, \text{ but}
$$
$$
\mu((x - \varepsilon, x + \varepsilon)) = 2\varepsilon > (\frac{2}{3})^n = \mu(C_n), \text{ a contradiction.}
$$
So such an $x \in C^\circ$ can't exist, and $C^\circ = \emptyset$.
Thus $(\overline{C})^\circ = C^\circ = \emptyset$, and $C$ is nowhere dense,
and since a meager set is a countable union of
nowhere dense sets, $C$ is meager. $\square$
Claim: $C$ is measure zero.
Measures are additive over disjoint sets, i.e.
$$
A \cap B = \emptyset \Rightarrow \mu(A \sqcup B) = \mu(A) + \mu(B),
$$
And if $A \subseteq B$, we have
$$
\mu(B) = \mu(B \sqcup (B \setminus A)) = \mu(B) + \mu(B \setminus A)
$$
$\Rightarrow \mu(B \setminus A) = \mu(B) - \mu(A).
$$

<!-- page 6 -->

Now let $B_n$ be the union of the intervals that are deleted at the $n^{th}$ step. We have

$$\mu(B_0) = 0$$

$$\mu(B_1) = 1/3$$

$$\mu(B_2) = 2(\frac{1}{9}) = 2/9$$

$$\mu(B_3) = 4(\frac{1}{27}) = 4/27$$

$$\therefore \mu(B_n) = 2^{n-1}/3^n$$

Moreover, if $i \neq j$, then $B_i \cap B_j = \emptyset$, and

$$C^c := [0, 1] - C = \bigsqcup_{i=1}^\infty B_i.$$

We thus have

$$\mu(C) = \mu([0, 1]) \cdot \mu(C^c)$$

$$= 1 - \mu(\bigsqcup_{n=1}^\infty B_n)$$

$$= 1 - \sum_{n=1}^\infty \mu(B_n)$$

$$= 1 - \sum_{n=1}^\infty 2^{n-1}/3^n$$

<!-- page 7 -->

$$\begin{array}{l} = 1 - (1/3) \sum_{n=0}^{\infty} (\frac{2}{3})^n \\ = 1 - (1/3) (1/1.2/3) \\ = 0. \end{array}$$

1c

Let $y \in [0,1]$ be arbitrary, we will produce an $x \in C$ such that $F(x) = c$.

Write $y = (a_1, a_2 \dots)_2 = \sum_{i=1}^{\infty} a_i 2^{-i}$ where $a_i \in \{0, 1\}$

Now define

$$x = (2a_1, 2a_2 \dots)_3 = \sum_{i=1}^{\infty} (2a_i) 3^{-i} := \sum_{i=1}^{\infty} b_i 3^{-i}$$

Since $a_i \in \{0, 1\}$, $b_i = 2a_i \in \{0, 2\}$, meaning $x$ has no $1^s$ in its ternary expansion and so $x \in C$.

Moreover, under $f$ we have

$$\left. \begin{array}{c} b_i \mapsto \frac{1}{2} b_i \\ \text{'' ''} \\ 2a_i \mapsto \frac{1}{2}(2a_i) = a_i \end{array} \right\} \begin{array}{l} \text{So } b_i \mapsto a_i \text{ and} \\ \text{thus } f(x) = y. \end{array}$$

So $C \to [0,1]$, which is uncountable, thus so is $C$.

<!-- page 8 -->

2a (⇒) Suppose X is G_S, so X = ⋃_{n=1}^∞ A_i with each A_i closed. Then A_i^c is open by definition, and so
X^c = (∪_{i=1}^∞ A_i)^c = ⋂_{i=1}^∞ A_i^c
is a countable intersection of open sets, and thus F_σ.
(⇐) Suppose X^c is an F_σ, so X^c = ⋂_{i=1}^∞ B_i with each B_i open. Then each B_i^c is closed by definition, and
X = (X^c)^c = (∪_{i=1}^∞ B_i)^c = ⋂_{i=1}^∞ B_i^c
is a countable union of closed sets, and thus G_S.
2b Suppose X is closed, we will show X = ⋂_{n=1}^∞ C_n with each C_n open. For each x∈X and n∈ℕ, define
• B_n(x) = {y ∈ ℝ^n | d(x,y) < 1/n}
• C_n = ⋃_{x∈X} B_n(x)
• W = ⋂_{n=1}^∞ C_n = ⋂_{n=1}^∞ ⋃_{x∈X} B_n(x)
Since each B_n(x) is open by construction and C_n is a union of opens, each C_n is open.

<!-- page 9 -->

Claim: $W = X$.

$X \subseteq W$: If $x \in X$, then $x \in B_n(x) \subseteq C_n$ for all $n$, and so $x \in \bigcap_{n=1}^{\infty} C_n = W$.

$W \subseteq X$: Suppose there is some $w \in W \setminus X$ (so $w \neq x$

for any $x \in X$) towards a contradiction.

Since $w \in \bigcap_{n=1}^{\infty} C_n$, $w \in C_n$ for every $n$. So $w \in \bigcup_{x \in X} B_n(x)$ for

every $n$. But then there is some particular $x_0 \in X$ such that

$w \in B_n(x_0)$ for every $n$ (otherwise we could take $N$ large enough

so that $w \notin B_N(x)$ for any $x \in X$, so $x \notin \bigcup_{x \in X} B_N(x)$) where $w \neq x_0$.

But then if $N_\varepsilon(x)$ is an arbitrary neighborhood of $x$,

We can take $\frac{1}{n} < \varepsilon$ to obtain $w \in B_n(x) \subseteq N_\varepsilon(x)$, which makes

w a limit point of $X$. But since $X$ is closed, it contains

its limit points, forcing the contradiction $w \in X$.

So $X$ is a countable intersection of open sets, and thus a $G_\delta$ set.

<!-- page 10 -->

Now suppose $X$ is open. Then $X^c$ is closed, and thus a $G_s$ set. But then $(X^c)^c = X$ is an $F_\sigma$ set by problem (2a).

2c Using the fact that singletons are closed in metric spaces, we can write $\mathbb{Q} = \bigcup_{q \in \mathbb{Q}} \{q\}$ as a countable union of closed sets, so $\mathbb{Q}$ is an $F_s$ set. Suppose $\mathbb{Q}$ was also a $G_s$ set, so $\mathbb{Q} = \bigcap_{i=1}^{\infty} A_i$ with each $A_i$ open. Then for any fixed $n$, $\mathbb{Q} \subseteq A_i$, so $A_i$ is dense in $\mathbb{R}$ for every $i$. However, it is also true that $\{q\}^c := \mathbb{R} \setminus \{q\}$ is an open, dense subset of $\mathbb{R}$, and we can write

$$\mathbb{R} \setminus \mathbb{Q} = \mathbb{R} \setminus \bigcup_{q \in \mathbb{Q}} \{q\} = \bigcap_{q \in \mathbb{Q}} (\mathbb{R} \setminus \{q\})$$

as in intersection of open dense sets; since $\mathbb{R}$ is a

Baire space, countable intersections of open dense sets are dense.

But then $(\bigcap_{i=1}^{\infty} A_i) \cap (\bigcap_{q \in \mathbb{Q}} \{q\}^c) = \mathbb{Q} \cap (\mathbb{R} \setminus \mathbb{Q}) = \emptyset$

must be dense in $\mathbb{R}$, which is absurd. ✕

<!-- page 11 -->

Note that this argument also works when $\mathbb{R}$ is replaced with any open interval $I$ and $\mathbb{Q}$ is replaced with $\mathbb{Q} \cap I$.

For a set that is neither $G_S$ nor $F_S$, consider

$$A = \mathbb{Q} \cap (0, \infty) \text{ , positive rationals}$$

$$B = (\mathbb{R} \setminus \mathbb{Q}) \cap (-\infty, 0) \text{ , negative irrationals}$$

A is $F_\sigma$ but not $G_S$, using above argument, and

dually B is $G_S$ but not $F_\sigma$.

Claim: $X = A \cup B$ is neither $G_S$ nor $F_\sigma$.

Suppose X is $G_S$. Then $X \cap \overbrace{(0, \infty)}^{open} = A$ is $G_S$ as well. ✱

Suppose X is $F_\sigma$. Then $X^c$ is $G_S$, but

$$X^c = (A \cup B)^c = A^c \cap B^c = (\mathbb{Q} \cap (-\infty, 0)) \cup ((\mathbb{R} \setminus \mathbb{Q}) \cap (0, \infty))$$

and thus $X^c \cap \overbrace{(-\infty, 0)}^{open} = A$ is $G_S$. ✱

So X is neither $G_S$ or $F_\sigma$.

<!-- page 12 -->

3a

Claim: $$c \in [0, 1] \Rightarrow \lim_{x \to c} f(x) = 0$$.

This holds iff $$\forall c \in I, \forall \varepsilon, \exists \delta$$ s.t. $$|x - c| < \delta \Rightarrow |f(x)| < \varepsilon$$,

so let $$\varepsilon > 0$$ be arbitrary. Consider the set

$$S = \{ n \in \mathbb{N} \mid \frac{1}{n} \geq \varepsilon \}$$, which is a finite set, and so

$$S_q = \{ r_n \in \mathbb{Q} \mid \frac{1}{n} \geq \varepsilon \}$$ is finite as well.

So choose $$\delta < \min_{r_n \in S_q} d(c, r_n)$$ so $$N_{\delta(c)} \cap S_q = \emptyset$$

Then $$|x - c| < \delta \Rightarrow \begin{cases} \cdot f(x) = 0 \text{ if } x \in I \setminus \mathbb{Q}, \text{ or} \\ \cdot x = r_m \in (\mathbb{Q} \setminus S_q) \cap I \text{ for some } m \text{ such that} \\ \frac{1}{m} < \varepsilon \text{ by construction.} \end{cases}$$

But then $$|f(x)| = \frac{1}{m} < \varepsilon$$ as desired. □

So $$\cdot c \in I \setminus \mathbb{Q} \Rightarrow f(c) = 0 = \lim_{x \to c} f(x),$$

$$\cdot c = r_n \in I \cap \mathbb{Q} \Rightarrow f(c) = \frac{1}{n} \neq 0 = \lim_{x \to c} f(x)$$

and $$f$$ is discontinuous on $$I \cap \mathbb{Q}$$. ■

<!-- page 13 -->

3b.1

Claim: $w_f$ is well defined

This amounts to showing that the sup and limit exist in

$$w_f(x) = \lim_{\delta \to 0^+} \sup_{y,z \in B_\delta(x)} |f(y) - f(z)|$$

Let $x \in \mathbb{R}$ be arbitrary and $\delta$ fixed.

Since $f$ is bounded, there is some $M$ such that

$$\forall y \in \mathbb{R}, |f(y)| < M, \text{ and so}$$

$$y, z \in \mathbb{R} \Rightarrow |f(y) - f(z)| = |f(y) + (-f(z))| \le |f(y)| + |-f(z)| = |f(y)| + |f(z)| < 2M,$$

which holds for $y, z \in B_\delta(x) \subseteq \mathbb{R}$ as well.

And so $\{|f(y) - f(z)| \text{ s.t. } y, z \in B_\delta(x)\}$ is bounded above and thus has

a least upper bound, and thus the following supremum exists.

$$S(\delta, x) = \sup_{y, z \in B_\delta(x)} |f(y) - f(z)|$$

To see that the $\lim_{\delta \to 0} S(\delta, x)$ exists, note that

$$\delta_1 \le \delta_2 \Rightarrow B_{\delta_1}(x) \le B_{\delta_2}(x)$$

and so for a fixed $x$, $S(\delta, x)$ is a monotonically

<!-- page 14 -->

decreasing function of $\delta$ that is bounded below by 0, which converges by the monotone convergence theorem. $\square$

Claim: $f$ is continuous at $x$ iff $w_p(x) = 0$.

($\Leftarrow$) Suppose $w_p(x) = 0$ and let $\varepsilon > 0$ be arbitrary; we will produce a $\delta$ to use in the definition of continuity.

Since $w_p(x) = \lim_{d \to 0^+} S(d, x) = 0$, we can choose $\delta$ such that

$$d < \delta \Rightarrow |S(d, x)| < \varepsilon, \quad \text{which means}$$

$$d < \delta \Rightarrow \sup_{y, z \in B_d(x)} |f(y) - f(z)| < \varepsilon$$

So fix $z=x$ and let $y$ vary, yielding

$$d < \delta \Rightarrow \sup_{y \in B_d(x)} |f(y) - f(x)| < \varepsilon$$

But now for an arbitrary $t \in B_\delta(x)$, we have $|x-t| < \delta$ and

$$|f(x) - f(t)| \le \sup_{y \in B_\delta(x)} |f(x) - f(y)| < \varepsilon,$$

which exactly says $|x-t| < \delta \Rightarrow |f(x) - f(t)| < \varepsilon$. $\square$

<!-- page 15 -->

(⇒) Suppose f is continuous at x and let ε > 0 be arbitrary; we will show ω_f(x) < ε.

Since f is continuous, choose δ such that

|x - y| < δ ⇒ |f(x) - f(y)| < ε/2.

We then have

y, z ∈ B_δ(x) ⇒ |x - y| < δ and |x - z| < δ,
⇒ |f(x) - f(y)| < ε/2 and |f(x) - f(z)| < ε/2
⇒ |f(y) - f(z)| ≤ |f(y) - f(x)| + |f(x) - f(z)| < ε/2 + ε/2 = ε,

and so

y, z ∈ B_δ(x) ⇒ |f(y) - f(z)| < ε ⇒ sup_{y, z ∈ B_δ(x)} |f(y) - f(z)| ≤ ε

⇒ S(δ, x) ≤ ε,

and since S(d, x) is monotonically decreasing in d,

ω_f(x) = lim_{d→0} S(d, x) ≤ S(δ, x) ≤ ε

as desired.

<!-- page 16 -->

3b.2

We will show that

$$A_{\varepsilon}^{c} = \{ x \in \mathbb{R} \mid w_{f}(x) < \varepsilon \}$$

is open by showing every point is an interior point.

Fix $\varepsilon > 0$ and let $x \in A_{\varepsilon}^{c}$ be arbitrary. We want to

produce a $\delta$ such that

$$B_{\delta}(x) \subsetneq A_{\varepsilon}^{c} \quad \text{or equivalently} \quad |y - x| < \delta \Rightarrow w_{f}(y) < \varepsilon.$$

Write $w_{f}(x) = \lim_{d \to 0^{+}} S(d, x)$; since $w_{f}(x) < \varepsilon$ and this limit

exists, we can choose $\delta$ such that

$$d < \delta \Rightarrow |S(d, x) - 0| < \varepsilon \Rightarrow |S(d, x)| < \varepsilon.$$

Now suppose $y \in B_{\delta}(x)$, so $|y - x| < \delta$. Then there exists some

$\delta'$ such that $B_{\delta}'(y) \subset B_{\delta}(x)$, and we claim that

$$S(\delta', y) \leq S(\delta, x)$$

Note that if this is true, then

$$w_{f}(y) = \lim_{d \to 0} S(d, y) \leq S(\delta', y) \leq S(\delta, x) < \varepsilon.$$

<!-- page 17 -->

To see why this is true, we just note that

$$\begin{array}{l} a, b \in B _ { S } ( y ) \subset B _ { S } ( x ) \Rightarrow a, b \in B _ { S } ( x ) \\ \Rightarrow \sup _ { a , b \in B _ { S } ( y ) } | f ( y ) - f ( z ) | \leq \sup _ { y , z \in B _ { S } ( x ) } | f ( y ) - f ( z ) | , \end{array}$$

since the supremum can only increase over a larger set.

So $w _ { f } ( y ) < \varepsilon$ as desired.

Finally, note that if $D _ { f } = \{ x \in \mathbb { R } \mid f \text { is discontinuous at } x \}$,

<!-- page 18 -->

④ Claim: $f$ is increasing, i.e. $x \le y \Rightarrow f(x) \le f(y)$

$F_{ix} \le \mathbb{R}$, and define

$$A_x = \{ t \in X \mid x > t \}, \quad A_x^c := \{ t \in X \mid x \le t \}.$$

(Note that $t \in A_x$ or $t \in A_x^c \Rightarrow t = x_n$ for some $n$, and $X = A_x \sqcup A_x^c$.)

Then noting that

$$x_n \in A_x \Rightarrow f_n(x) \equiv 1$$

$$x_n \in A_x^c \implies f_n(x) \equiv 0,$$

We can write

$$f(x) = \sum_{n=1}^{\infty} \frac{1}{n^2} f_n(x) = \sum_{\{n \mid x_n \in A_x\}} \frac{1}{n^2} \cdot 1 + \sum_{\{n \mid x_n \in A_x^c\}} \frac{1}{n^2} \cdot 0$$
$$= \sum_{\{n \mid x_n \in A_x\}} \frac{1}{n^2}.$$

Now if $y \ge x$, then $y \ge t$ for every $t \in A_x$, so $A_y \ge A_x$.

<!-- page 19 -->

But then

$$f(x) = \sum_{\{n \mid x_n \in A_x\}} \frac{1}{n^2} \leq \sum_{\{n \mid x_n \in A_y\}} \frac{1}{n^2} = f(y),$$

where the inequality holds because

$$\begin{array}{l} A_x \leq A_y \Rightarrow \{n \mid x_n \in A_x\} \leq \{n \mid x_n \in A_y\} \\ \Rightarrow |\{n \mid x_n \in A_x\}| \leq |\{n \mid x_n \in A_y\}|, \end{array}$$

so the latter sum has at least as many terms and everything is positive. So $f(x) \leq f(y)$.

Claim: $f$ is continuous on $\mathbb{R} \setminus X$ since

$$\sum f_n \xrightarrow{u} f \text{ and each } f_n \text{ is continuous there.}$$

Since $|f_n(x)| \leq 1$ by definition, and

$$|f_{n(x)}/n^2| \leq |1/n^2| := M_n \text{ where } \sum M_n < \infty,$$

$$\sum f_n \xrightarrow{u} f \text{ by the } M \text{ test.}$$

Note that for a fixed $n$, $D_{f_n} = \{x_n\}$. This is

<!-- page 20 -->

because if we take a sequence $\{y_i\} \to X_n$ with each

$y_i > X_n$, then $f(y_i) = 1$ for every $i$, and

$$\lim_{i \to \infty} f(y_i) = \lim_{i \to \infty} 1 = 1 \neq f(\lim_{i \to \infty} y_i) = f(X_n) = 0$$

So $f_n$ is not continuous at $X = X_n$. Otherwise, either

$X > X_n$ or $X < X_n$, in which case we can let $\varepsilon$ be

arbitrary and choose $S < |X - X_n|$ to get

$$y \in B_S(X) \Rightarrow \begin{cases} y > X_n & \Rightarrow |f(y) - f(x)| = |0 - 0| < \varepsilon \\ y < X_n & \Rightarrow |f(y) - f(x)| = |1 - 1| < \varepsilon. \end{cases}$$

Letting $F_N = \sum_{n=1}^N f_n$, we find that

$$F_N = \begin{cases} f_1 + f_2 + \dots + f_N \\ \uparrow \quad \uparrow \quad \uparrow \\ \text{discontinuous at: } \{x_1\} \cup \{x_2\} \cup \dots \cup \{x_N\} \end{cases} \quad \begin{cases} S_0 & F_N \text{ is continuous on} \\ \mathbb{R} \setminus \bigcup_{i=1}^N \{x_N\}. \end{cases}$$

and since $\mathbb{R} \setminus X \subseteq \mathbb{R} \setminus \bigcup_{i=1}^N \{x_N\}$, $F_N$ is continuous there too.

But then $f = \text{uniform limit}(F_N)$ is continuous on $\mathbb{R} \setminus X$.

<!-- page 21 -->

⑤a Let X = (C(I), ||·||∞) where I = [0, 1],

C(I) = {f : I → R | f is continuous}, and

d(f, g) = ||f - g||∞ = sup_{x∈I} |f(x) - g(x)|.

Claim: X is a metric space.

1) d(f, g) = 0 ⇒ f = g

If sup_{x∈I} |f(x) - g(x)| = 0 then |f(x) - g(x)| = 0 ∀x ∈ R,

so f(x) = g(x) ∀x ∈ R and f = g.

2) d(f, g) = d(g, f)

We have d(f, g) = sup_{x∈I} |f(x) - g(x)|

sup_{x∈I} |g(x) - f(x)|

= d(g, f).

3) d(f, h) ≤ d(f, g) + d(g, h)

We have d(f, g) = sup_{x∈I} |f(x) - g(x)|

= sup_{x∈I} |f(x) - h(x) + h(x) - g(x)|

<!-- page 22 -->

$$\begin{array}{l} \leq \sup _ {x \in I} \left( \left| f (x) - h (x) \right| + \left| h (x) - g (x) \right| \right) \stackrel {\Delta - i n e q} {\sim} \frac {\text { in } \mathbb {R}}{} \\ = \sup _ {x \in I} | f (x) - h (x) | + \sup _ {x \in I} | h (x) - g (x) | \\ = d (f, h) + d (h, g). \end{array}$$

So $X$ is a metric space. $\square$

Claim: $X$ is complete.

Let $\{f_i\}$ be a Cauchy sequence in $X$, we will show that it

converges in $X$. Since $\{f_i\}$ is Cauchy in $X$, we have

$$\forall \varepsilon > 0, \exists N _ {o} | n \geq m \geq N _ {o} \Rightarrow \| f _ {n} - f _ {m} \| _ {\infty} < \varepsilon$$

First we will define a candidate limit function $f$, then show $f \in X$.

1) Define $f := \lim_{n \to \infty} f_n$ by $f(x) = \lim_{n \to \infty} f_n(x)$.

This is well-defined; let $S_x = \{f_i(x)\} \subseteq \mathbb{R}$ for a fixed $x$,

and we claim $S_x$ is Cauchy in $\mathbb{R}$, which is complete.

This follows because if $\{f_i\}$ is Cauchy in $X$, then

$$\left| f _ {n} (x) - f _ {m} (x) \right| \leq \sup _ {x \in I} \left| f _ {n} (x) - f _ {m} (x) \right| = \left\| f _ {n} - f _ {m} \right\| _ {\infty} \rightarrow 0.$$

<!-- page 23 -->

2) $f \in X$, for which it suffices to show $f$ is continuous.

Let $\varepsilon > 0$, and since $\{f_i\}$ is Cauchy, choose $N_0$ large s.t.

$$n \ge N_0 \Rightarrow \|f_n - f\|_\infty < \frac{\varepsilon}{3}.$$

Now fix $n \ge N_0$; since $f_n$ is continuous, choose $\delta$ such that

$$|x - y| < \delta \Rightarrow |f_n(x) - f_{n(y)}| < \frac{\varepsilon}{3}$$

Then

$$|x - y| < \delta \Rightarrow |f(x) - f(y)| = |f(x) - f_{n(x)} + f_{n(x)} - f_{n(y)} + f_{n(y)} - f(y)|$$

$$\le |f(x) - f_{n(x)}| + |f_{n(x)} - f_{n(y)}| + |f_{n(y)} - f(y)|$$

$$\le \sup_{x \in I} |f(x) - f_{n(x)}| + |f_{n(x)} - f_{n(y)}| + \sup_{y \in I} |f_{n(y)} - f(y)|$$

$$= \|f - f_n\|_\infty + |f_{n(x)} - f_{n(y)}| + \|f_n - f\|_\infty$$

$$\le \frac{\varepsilon}{3} + \frac{\varepsilon}{3} + \frac{\varepsilon}{3} = \varepsilon,$$

So $f$ is continuous, $f = \lim f_n \in X$, and $X$ is complete.

<!-- page 24 -->

5b

Let $B = \{f \in X \mid \|f\|_{\infty} \leq 1\}$

Claim: $B$ is closed.

Let $f$ be a limit point of $B$, so there is some sequence

$f_n \to f$ in $X$ with each $f_n \in B$ so $\|f_n\|_{\infty} \leq 1 \forall n$.

Let $\varepsilon > 0$, and since $f_n \to f$ in $X$, choose $N_0$ such that

$$n \geq N_0 \Rightarrow \|f_n - f\| < \varepsilon$$

Then,

$$\begin{array}{l} \|f\|_{\infty} = \|f - f_n + f_n\|_{\infty} \\ \leq \|f - f_n\|_{\infty} + \|f_n\|_{\infty} \\ < \varepsilon + 1, \end{array}$$

and taking $\varepsilon \to 0$ yields $\|f\|_{\infty} \leq 1$. $\blacksquare$

Claim: $B$ is bounded

A subset $B \subseteq X$ is bounded iff there is some $x \in X$ and

some $r > 0$ in $\mathbb{R}$ where $B \subset N(r, x) = \{y \in X \mid d(y, x) < r\}$.

Choose $x=0$, $r=2$, then $f \in B \Rightarrow d(f, 0) = \|f - 0\|_{\infty} = 1 < 2$, so $f \in N(2, 0)$.

<!-- page 25 -->

Claim: B is not compact.

Since B is a metric space, B is compact iff B is sequentially compact.

Define $f_n$ as the triangle:

![img-0.jpeg](img-0.jpeg)

Then $f_n \xrightarrow{R} f$ where $f(x) = \begin{cases} 1, & x=0 \\ 0, & x \in (0,1], \end{cases}$

and so $\forall n, \|f_n - f\|_\infty = 1$, attained at $x=0$. So $\lim_{n \to \infty} \|f_n - f\|_\infty \neq 0$,

and $\{f_n\}$ does not converge in X, nor can any subsequence.

Claim: B is not totally bounded.

If it were, $\forall \varepsilon$ there would exist a finite collection

$\{g_i\}_{i=1}^N \subseteq B$ such that $B \subseteq \bigcup_{i=1}^N N(\varepsilon, g_i)$ where

$$N(\varepsilon, g_i) = \{h \in B \mid \|h - g_i\| < \varepsilon\}.$$

Note that if $h_1, h_2 \in N(\varepsilon, g_i)$ then $\|h_1 - h_2\| \leq \|h_1 - g\| + \|g - h_2\| < 2\varepsilon$.

<!-- page 26 -->

So choose $\varepsilon=\frac{1}{2}$, and consider the collection $\{f_n\}_{n=1}^{\infty}$.

Since $\|f_n-f_m\|=1$, each $N(\varepsilon, g_i)$ can contain at most one

$f_n$, since $f_n, f_m \in N(\varepsilon, g_i)$ for $n \neq m$ would

imply $\|f_n-f_m\|_\infty < 2\varepsilon = 2(\frac{1}{2}) = 1$. But there are finitely

many $N(\varepsilon, g_i)$ and infinitely many $f_n$, so if this is

a cover of $B$, so $N(\varepsilon, g_i)$ must contain at least $2f_n^s$. ✕

6a Claim: If $\sum g_n \xrightarrow{u} G$, then $g_n \xrightarrow{u} O$.

Let $G_N = \sum_{n=1}^N g_n$ and $G = \lim_{N \to \infty} G_N$.

Suppose $G_N \xrightarrow{u} G$, then choose $N$ large enough so that

$$\forall x \in X, n \geq N \Rightarrow |G_n(x) - G(x)| < \frac{\varepsilon}{2}$$

Then letting $n > n-1 > N$, we have

$$\begin{aligned} |g_n(x)| &= \left| \sum_{i=1}^n g_i(x) - \sum_{i=1}^{n-1} g_i(x) \right| \\ &= \left| \left( \sum_{i=1}^n g_i(x) - G(x) \right) - \left( \sum_{i=1}^{n-1} g_i - G(x) \right) \right| \\ &\leq \left| \sum_{i=1}^n g_i(x) - G(x) \right| + \left| \sum_{i=1}^{n-1} g_i - G(x) \right| \\ &\leq \frac{\varepsilon}{2} + \frac{\varepsilon}{2} = \varepsilon, \end{aligned}$$

<!-- page 27 -->

$$S _ { 0 } \quad \forall x \in X , | g _ { n } ( x ) | < \varepsilon \Rightarrow g _ { n } \stackrel { u } { \rightarrow } 0 . \quad \square$$

Now let $g _ { n } = 1 / 1 + n ^ { 2 } x$ , we'll show $g _ { n }$ does not converge to 0 uniformly.

Note $g _ { n } \stackrel { u } { \rightarrow } g$ iff $\forall \varepsilon , \exists N _ { 0 } | \forall x , n \geq N _ { 0 } \Rightarrow | g _ { n } ( x ) - g ( x ) | < \varepsilon$ ,

so let $\varepsilon < \frac { 1 } { 2 }$ , $N _ { 0 }$ be arbitrary, and choose $x _ { 0 } < 1 / N _ { 0 } ^ { 2 }$ . Then,

$$| g _ { N _ { 0 } } ( x _ { 0 } ) | = \frac { 1 } { | 1 + N _ { 0 } ^ { 2 } x | } = \frac { 1 } { | 1 + N _ { 0 } ^ { 2 } ( 1 / N _ { 0 } ^ { 2 } ) } = \frac { 1 } { 2 } > \varepsilon .$$

Claim: $g$ is continuous on $( 0 , \infty )$ .

Let $x \in ( 0 , \infty )$ be arbitrary, and choose $a < x$ . We will show

$g$ converges uniformly on $[ a , \infty )$ , and since each $g _ { n }$ is continuous

on $[ a , \infty )$ as well, $g$ will be the uniform limit of continuous

functions and thus continuous itself.

We can use the M-test. Since $x > a$ ,

$$| 1 / 1 + n ^ { 2 } x | \leq | 1 / n ^ { 2 } x | \leq | 1 / n ^ { 2 } a | = \frac { 1 } { a } | \frac { 1 } { n ^ { 2 } } | ,$$

$$\text { where } \sum _ { n = 1 } ^ { \infty } \frac { 1 } { a } \frac { 1 } { n ^ { 2 } } = \frac { 1 } { a } \sum \frac { 1 } { n ^ { 2 } } < \infty ,$$

So $g$ converges uniformly on $[ a , \infty )$ .

<!-- page 28 -->

6b

Claim: g is differentiable on (0,∞).

If g'(x) exists, we have

$$\begin{array}{l} g'(x) = \lim_{a \to x} (x-a)^{-1} (g(x) - g(a)) \\ = \lim_{a \to x} (x-a)^{-1} \sum_{n=1}^{\infty} \frac{-n^2(x-a)}{(1+n^2x)(1+n^2a)} \\ = \lim_{a \to x} \sum_{n=1}^{\infty} \frac{-n^2}{(1+n^2x)(1+n^2a)} \\ = \sum (-n^2)/(1+n^2x)^2, \end{array}$$

which exists because it converges uniformly on [a, ∞), as

$$\left| \frac{-n^2}{(1+n^2x)^2} \right| \le \left| \frac{n^2}{(n^2x)^2} \right| = \left| \frac{1}{n^2x^2} \right| \le \left| \frac{1}{a^2n^2} \right| := M_n$$

where $\sum M_n = \sum \frac{1}{a^2n^2} = \frac{1}{a^2} \sum \frac{1}{n^2} < \infty$.

So g is continuously differentiable on (0,∞).

<!-- page 29 -->

⑦a Claim: $h_n \xrightarrow{u} 0$ on $[0, \infty)$

Note that $h_n'(x) = \frac{1-nx}{(1+x)^n} \Rightarrow h_n' = 0$ iff $x=1/n$ and

$$h_n''(x) = \frac{1+x+nx}{nx^2(1+x)^{n-1}} \text{ and } h_n''(\frac{1}{n}) < 0,$$

so $x=\frac{1}{n}$ is a global maximum and thus

$$\forall x, |h_n(x)| \le |h_n(\frac{1}{n})| = \left| \frac{1/n}{(1+\frac{1}{n})^n} \right| = \frac{1}{n(1+\frac{1}{n})^n} \le \frac{1}{2n} \quad \text{for } n > 1$$

$$\text{so } \sup_{x \in [0, \infty)} |h_n(x)| = |h_n(\frac{1}{n})| = O(\frac{1}{n}) \to 0, \text{ thus } \|h_n\|_\infty \to 0$$

and $h_n \to 0$ uniformly.

⑦b Let $h(x) = \sum_{n=1}^{\infty} h_n(x) = \sum_{n=1}^{\infty} x/(1+x)^{n+1}$

i) Demonstrably, $h(0)=0$, and for a fixed $x$ we have

$$\begin{aligned} h(x) &= \sum_{n=1}^{\infty} x/(1+x)^{n+1} = (x/1+x) \sum_{n=1}^{\infty} (1/1+x)^n \\ &= \frac{x}{1+x} \left( \frac{1}{1-(1/1+x)} \right) \quad \text{since } x > 0 \Rightarrow \\ &= 1. \quad \square \end{aligned}$$

<!-- page 30 -->

ii) It can not converge uniformly on $[0, \infty)$, otherwise $h$ would be the uniform limit of continuous functions, but $h$ is discontinuous.

7c

Let $a > 0$ and $X = [a, \infty)$.

Claim: $\sum h_n \xrightarrow{u} h$ on $X$.

Since $x > a$, we have

$$(1+x)^{n+1} = \sum_{j=1}^{n} (\binom{n}{j})x^j \quad \Rightarrow 1+nx+n^2x^2$$

$x > a > 0$, so positive terms.

$$|h_{n(x)}| = \left| \frac{x}{(1+x)^{n+1}} \right| \leq \left| \frac{x}{1+nx+n^2x^2} \right| \leq \left| \frac{a}{1+nx+n^2} \right| \leq \left| \frac{a}{n^2a^2} \right| = \left| \frac{1}{n^2a} \right|$$

So let $M_n = 1/2n^2$, then $\sum M_n < \infty \Rightarrow \sum h_n \xrightarrow{u} h$

by the $M$ test.

<!-- page 31 -->

Zack
Garza

① Suppose E is bounded, so diam(E) ≤ M for some fixed

M. In particular, if Q_i ≤ E is an interval, then

|Q_i| ≤ M. Let ε > 0, and choose {Q_i} → E s.t.

for each i, |Q_i| ≤ ε/2M

i.e. E ≤ U_i E_i

Then let L_i = Q_i^2. We then have

|L_i| ≤ |b² - a²| = |b - a| · |b + a| = |Q_i| · |b + a|

≤ |Q_i| · 2M

≤ (ε/2^(i+1)M) 2M

= ε/2^i,

so Σ_{i=1}^∞ |L_i| ≤ Σ_{i=1}^∞ ε/2^i = ε, and {L_i} → E², so

m_*(E²) < ε → 0.

Claim: It suffices to consider the bounded case.

Ball of radius n around 0

PF If E is not bounded, consider F_n = E ∩ B(n, 0).

Then F_n is bounded (by n), and since F_n ≤ E ⇒ m_*(F_n) ≤ m_*(E) = 0

by subadditivity, m_*(F_n²) = 0 by the bounded case.

<!-- page 32 -->

But then $$E^2 = \bigcup_{n=1}^{\infty} F_n^2 \Rightarrow m_*(E^2) = m(\bigcup_{n=1}^{\infty} F_n^2) \leq \sum_{n=1}^{\infty} m_*(F_n^2) = 0$$

by countable subadditivity.

# ② Note

1) \(E_{1} = E_{1}\backslash E_{2}\sqcup E_{1}\cap E_{2}\)
2) \(E_{2} = E_{2}\backslash E_{1}\sqcup E_{1}\cap E_{2}\)
3) \(E_{1} \triangle E_{2} = E_{2} \backslash E_{1} \sqcup E_{1} \backslash E_{2}\)
4) \(E_{1} \cup E_{2} = (E_{1} \triangle E_{2}) \sqcup (E_{1} \cap E_{2})\)

All disjoint unions, so we can freely apply measures and use countable additivity.

so

$$\begin{array}{l} m(E_1) + m(E_2) = m(E_1 \setminus E_2) + m(E_1 \cap E_2) \\ \quad + m(E_2 \setminus E_1) + m(E_1 \cap E_2) \\ = m(E_1 \triangle E_2) + m(E_1 \cap E_2) + m(E_1 \cap E_2) \\ = m(E_1 \cup E_2) + m(E_1 \cap E_2). \end{array}$$

<!-- page 33 -->

3a) Suppose $m(A)=m(B)<\infty$.

Since $A \subseteq E \subseteq B$, we have $\underline{E \setminus A \subseteq B \setminus A}$. However,

$$B = A \sqcup (B \setminus A) \Rightarrow m(B) = m(A) + m(B \setminus A)$$

$$\Rightarrow m(B) - m(A) = m(B \setminus A)$$

(since $m(A)<\infty$)

$$\Rightarrow m(B \setminus A) = 0$$

(since $m(B)=m(A)$)

So $m_{*}(E \setminus A) = 0$ by subadditivity.

But then

$E = A \sqcup (E \setminus A)$, where $A$ is measurable by assumption and $E \setminus A$ is an outer measure $0$ set and thus measurable.

So $E$ is measurable, and

$$m(E) = m(A) + m(E \setminus A)$$

$$= m(A) + 0$$

$$\Rightarrow m(E) = m(A) = m(B) < \infty.$$

<!-- page 34 -->

3b) Idea: $[0,1] \subseteq \mathcal{N} \subseteq [-1,2]$, so take

- $A = (-\infty, 0)$

- $E = A \cup (\mathcal{N} + 1)$, where $\mathcal{N}$ is the non-measurable set, and
- $B = \mathbb{R}$
$\mathcal{N} + 1 = \{x + 1 \mid x \in \mathcal{N}\}$ is non-measurable by the same argument used for $\mathcal{N}$.

Claim: $E$ is not measurable.

Supposing it were, note that $A^c$ is measurable,

and countable intersections of measurable sets are

measurable, so

$$E \cap A^c = (A \cup (\mathcal{N} + 1)) \cap A^c = \mathcal{N} + 1$$

must be measurable. ✕

4) Let $A, B$ be fixed, and define

$$E_t := \{x \in \mathbb{R}^n \mid \inf_{a \in A} |x-a| \le t\} \cap B$$

$$= \{x \in \mathbb{R}^n \mid \text{dist}(x, A) \le t\} \cap B$$

and
$$f: \mathbb{R} \to \mathbb{R}$$
$$t \mapsto \mu(E_t)$$

<!-- page 35 -->

Note that $E_0 = A$, so $f(0) = \mu(A)$, and since $B$ is compact

and thus banded, there is some $t = T$ such that $B \subseteq E_T$.

So $f$ maps $[0, T]$ to $[\mu(A), \mu(B) + M]$ for some $M$.

Claim: $f$ is cts, and for all $t \in [0, T']$ for some $T'$, $A \subseteq E_t \subseteq B$ and

each $E_t$ is compact.

Note that if this is true, we can first apply the

intermediate value theorem to find a $T'$ such that

$f(T') = m(B)$, then restrict $f$ to map $[0, T']$

to $[m(A), m(B)]$. We can apply it again to pull back any

$c \in [m(A), m(B)]$ to a $t$ satisfying $c = f(t) = \mu(E_t)$, in

which case $A \subseteq E_t \subseteq B$ and $\mu(A) \subseteq c = \mu(E_t) \subseteq \mu(B)$ as desired.

$\cdot$ $f$ is cts. We'll show that the 2-sided limit $\lim_{t_i \to t} f(t_i)$ exists and

is equal to $f(t)$, using the fact that $a \le b \Rightarrow E_a \le E_b$.

If $t_i \ne t$, then $E_{t_1} \le E_{t_2} \le \dots \le E_t$, and $\bigcup_{i \in \mathbb{N}} E_{t_i} = E$, so

<!-- page 36 -->

by continuity of measure from below, we have $\lim_{i \to \infty} \mu(E_{t_i}) = \mu(E)$, so

$$\lim_{t_i \to t} f(t_i) = \lim_{i \to \infty} \mu(E_{t_i}) = \mu(E_t) = f(t).$$

Similarly, if $t_i \to t$, noting that $t_i \le T' \Rightarrow t_i \le T' \Rightarrow \mu(E_{t_i}) \le \mu(B) < \infty$,

$$\text{and} \quad E_{t_1} \ge E_{t_2} \ge \dots \ge E, \text{ so}$$

we can apply continuity of measure from above to obtain

$$\lim_{t_i \to t} f(t_i) = \lim_{i \to \infty} \mu(E_{t_i}) = \mu(E_t) = f(t).$$

So $f$ is cts.

- $E_t$ is compact:

Since $E_t \subseteq B$ which is compact and thus bounded, it suffices to show that

$E_t$ is closed. But letting $N_t = \{x \in \mathbb{R}^n \mid \text{dist}(x, A) < t\}$, we have

$$E_t = \overline{N_t \cap B}, \text{ where } N_t \text{ is open because } N_t = \bigcup_{a \in A} \underbrace{\{x \in \mathbb{R}^n \mid \text{dist}(x, a) < r\}}_{\text{Open ball around a}}, \text{ and}$$

$N_t \subseteq B \Rightarrow N_t \cap B$ is still open. But the closure of any open set is closed.

- $t \in [0, T'] \Rightarrow A \subseteq E_t \subseteq B$:

$E_0 = A$ and $t \le s \Rightarrow E_t \subseteq E_s$, so $A \subseteq E_t$ for all $t$.

But $E_t = \overline{N_t \cap B} \subseteq \overline{B} = B$ since $B$ is closed, so $E_t \subseteq B$ for all $t$ as well.

<!-- page 37 -->

5a) Recalling that $N$ is constructed by considering $\frac{R \cap [0,1)}{Q \cap [0,1)}$ and taking exactly one element from each equivalence class, we can note that if $E \subseteq N$, then $E$ contains a choice of at most one element from each equivalence class. We can then take a similar enumeration $Q \cap [-1,1] = \{q_i\}_{i=1}^{\infty}$ and define $E_j := E + q_j$.

Then $E \subseteq N \Rightarrow \bigsqcup_{j \in N} E_j \subseteq \bigsqcup_{j \in N} N_j \subseteq [-1, 2]$, and since

$E$ is measurable, we must have

$$\mu(E) = \mu(\bigsqcup_{j \in N} E_j) = \sum_{j \in N} \mu(E_j) = \sum_{j \in N} \mu(E) \le 3,$$

which can only hold if $m(E) = 0$. $\square$

5b) Suppose $\mu(I \setminus N) < 1$, so $m(I \setminus N) = 1 - 2\varepsilon$ for

some $\varepsilon > 0$. Then choose an open $G \supseteq I \setminus N$ such

that $\mu(G) = \mu(I \setminus N) + \varepsilon = 1 - \varepsilon$. Then $I \setminus G \subseteq N$,

<!-- page 38 -->

and so by (1) we must have $\mu(I \setminus G) = 0$. But then

$$I = G \sqcup I \setminus G \Rightarrow \mu(I) = \mu(G) + \mu(I \setminus G)$$

$$\Rightarrow 1 = 1 - \varepsilon < 1, \text{ a contradiction. } \square$$

5c) Let

$$\left. \begin{array}{l} E_1 = N \\ E_2 = I \setminus N \end{array} \right\} \Rightarrow I = E_1 \sqcup E_2$$

but $m_*(E_1) = m_*(N) > 0$, otherwise $N$ would be

measurable so $m_*(E_1 \sqcup E_2) = 1$ but

$$m_*(E_1) + m_*(E_2) = 1 + \varepsilon \text{ for some } \varepsilon > 0.$$

6a) Claim: $E$ is a countable union of a countable intersection of measurable sets, and thus measurable.

Proof: Write $E = \{x \mid x \in E_j \text{ for infinitely many } j\}$, the claim is that $E = \bigcap_{j=1}^{\infty} \bigcup_{k=j}^{\infty} E_j$.

$$\cdot E \subseteq \bigcap_{j=1}^{\infty} \bigcup_{k=j}^{\infty} E_j: \text{Suppose } x \text{ is in infinitely many } E_j. \text{ Then for any fixed}$$

$K$, there is some $M \ge K$ such that $x \in E_M \subseteq \bigcup_{j=k}^{\infty} E_j := S_k$. But this happens for every $K$,

<!-- page 39 -->

so $x \in \bigcap_{k=1}^{\infty} S_k$. $\square$

$\cdot E \ge \bigcap_{j=1}^{\infty} \bigcup_{k=j}^{\infty} E_j : \text{Suppose } x \in \bigcup_{j=k}^{\infty} E_j \text{ for every } k. \text{ Then if } x \text{ were in only finitely}$

many $E_j$, we could pick a maximal $E_M$ such that $K \ge M \Rightarrow x \in E_K$, and so

$x \in \bigcup_{j=M}^{\infty} E_j$ - a contradiction. $\square$

Claim: $m(E) = 0$

We'll use the fact that $\sum_{n=1}^{\infty} a_n < \infty \Rightarrow \lim_{j \to \infty} \sum_{n=j}^{\infty} a_n = 0$, i.e. the tails

of a convergent sum must become arbitrarily small.

Since $E = \bigcap_{k=1}^{\infty} \bigcup_{j=k}^{\infty} E_j$, $E \subseteq \bigcup_{j=k}^{\infty} E_j$ for all $k$. So $m(E) \subseteq \sum_{j=k}^{\infty} E_j \to 0$,

forcing $m(E) = 0$. $\blacksquare$

(6b) Fix $x$ and let $E_{p,j} = \{ x \in \mathbb{R} \mid |x - p_j| \le 1/j^3 \}$

and $E_j = \bigcup_{\substack{p \text{ coprime} \\ \text{to } j}} E_{p,j} \subseteq \bigcup_{p=1}^{j} E_{p,j}$, and since $E_{p,j} \subseteq B(1/j^3, p_j)$,

$m(E_{p,j}) \le 2/j^3$ and thus $m(E_j) \le q(2/j^3) = 2/j^2$.

But then $\sum_{j=1}^{\infty} m(E_j) \le \sum_{j=1}^{\infty} 2/j^2 < \infty$. Moreover,

<!-- page 40 -->

E=big[0]0.5[0]0.5[0]0.5[0]0.5[0]0.5[0]0.5[0]0.5[0]0.5[0]0.5[0]0.5[0]0.5[0]0.5[0]0.5[0]0.5[0]0.5[0]0.5[0]0.5[0]

Which is precisely the set we want. So by (1), m(E)=0.

<!-- page 41 -->

Analysis HW 3

Zack Garza

⑬ If $m_*(E)$, take $B = \mathbb{R}^n$, otherwise suppose $m_*(E) < \infty$ and let $\varepsilon > 0$. Choose $\{Q_i\} \Rightarrow E$ then choose open $\{L_i\}$ s.t. $Q_i \subseteq L_i$ and $|L_i| < (m_*(E) + \varepsilon)/2^i$.

Then define $L(\varepsilon) = \bigcup_{i=1}^n L_i$; then $L(\varepsilon)$ is open (and thus Borel) and

$$m(L(\varepsilon)) = m_*(L(\varepsilon)) \leq \sum_{i=1}^\infty |L_i| < m_*(E) + \varepsilon.$$

So take the sequence $\varepsilon_k = \frac{1}{k} \to 0$; then let $\boxed{L^n = \bigcap_{k=1}^n L_{\nu_k}}$. We have $L^{k+1} \subseteq L^k \forall k,$ and $m(L^2) \leq m_*(E) + 1 < \infty$, so $L^n \searrow E$ and by upper continuity of measure,

$$m(\bigcap_{n=1}^\infty L^n) = m(\bigcap_{k=1}^\infty L_{\nu_k}) = \lim_{k \to \infty} m(L_{\nu_k}) = \lim_{k \to \infty} m_*(E) + \frac{1}{k} = m_*(E),$$

so take $\boxed{B = \bigcap_{n=1}^\infty L^n}$.

⑭ Let $\varepsilon > 0$; since $E \in \mathcal{J}(\mathbb{R}^n)$, there exists a closed set $K_\varepsilon$ s.t. $m(E \setminus K_\varepsilon) < \varepsilon$. If $m(E) < \infty$, then $m(K_\varepsilon) = m(E) - \varepsilon$, so take the sequence $\varepsilon_n = \frac{1}{n}$ and let $\boxed{K^n = \bigcup_{i=1}^n K_{\nu_i}}$, then $K^n \subseteq K^{n+1} \forall i$ and $K^n \nearrow E$, so by continuity of measure from below,

$$m(\bigcup_{n=1}^\infty K^n) = \lim_{n \to \infty} m(K^n) = \lim_{n \to \infty} m(E) - \frac{1}{n} = m(E),$$

so take $\boxed{B = \bigcup_{n=1}^\infty K^n}$, which is a countable union of closed sets and thus Borel.

If $m(F) = \infty$, let $E_n = E \cap \overline{B(n, 0)}$. Then $\exists B_n$ (by the bounded case) such that

$B_n \subseteq E_n$ is closed and $m(B_n) = m(E_n)$. But $E_n \nearrow E$, so

$$m(E) = m(\bigcup_{n=1}^\infty E_n) = \lim_{n \to \infty} m(E_n) = \lim_{n \to \infty} m(B_n) = m(\bigcup_{n=1}^\infty B_n),$$

so take $B = \bigcup_{n=1}^\infty B_n$, which is borel since each $B_n$ is.

⑮ Since $m(E) = m_*(E)$, choose $\{Q_j\} \Rightarrow E$ closed cubes such that $\sum_{j=1}^\infty |Q_j| < m(E) + \varepsilon/2$. Since $\sum_{i=1}^\infty |Q_i|$ converges, choose $N$ such that $\sum_{i=N}^\infty |Q_i| < \varepsilon/2$, and let $\boxed{A = \bigcup_{i=1}^{N-1} Q_i}$. Then,

$$E \triangle A = (\underbrace{E \setminus \bigcup_{i=1}^{N-1} Q_i}_{\text{}}) \sqcup (\underbrace{\bigcup_{i=1}^{N-1} Q_i}_{\text{}} \setminus E)$$

$$\leq \bigcup_{i=N}^\infty Q_i \quad \bigsqcup_{i=1}^N (\bigcup_{i=1}^\infty Q_i \setminus E)$$

$$\Rightarrow m(E \triangle A) \leq m(\bigcup_{i=N}^\infty Q_i) + (m(\bigcup_{i=1}^N Q_i) - m(E)) \leq \varepsilon/2 + ((m(E) + \varepsilon/2) - m(E)) = \varepsilon.$$

<!-- page 42 -->

②a Choose an open set \(\mathbb{O} \Rightarrow E\) s.t. \(m_{*}(\mathbb{O}) < (1/1 - \varepsilon)m_{*}(E)\), so that \((1 - \varepsilon)m_{*}(\mathbb{O}) < m_{*}(E)\). Then write \(\mathbb{O} = \bigsqcup_{i=1}^{\infty} Q_{i}\) with each \(Q_{i}\) a closed cube, then towards a contradiction suppose that \(m(E \cap Q_{i}) < (1 - \varepsilon)m(Q_{i})\) \(\forall i\). Then, writing \(E = \bigsqcup_{i=1}^{\infty}(E \cap Q_{i})\), we have \(m(E) = \sum_{i=1}^{\infty} m(E \cap Q_{i}) < \sum_{i=1}^{\infty}(1 - \varepsilon)m(Q_{i}) = (1 - \varepsilon)m(\bigsqcup_{i=1}^{\infty} Q_{i}) = (1 - \varepsilon)m(\mathbb{O}) < m(E)\) so we must have \(m(E \cap Q_{j}) \geq (1 - \varepsilon)m(Q_{j})\) for some \(j\).  
②b Let \(\varepsilon > 0\) be arbitrary, and by (a) choose \(Q\) such that \(m(E \cap Q) \geq (1 - \varepsilon)m(Q)\). Then let \(E_{0} = E \cap Q \subseteq E\), so \(E_{0} - E_{0} \subseteq E - E\), and supposing towards a contradiction that \(E_{0} - E_{0}\) contains no ball around \(0\), choose \(d << 1\) such that \(d \notin E_{0} - E_{0}\), and thus \(E_{0} \cap E_{0} + d = \emptyset\). Also choose \(d\) small enough that \(m(Q \cup Q + d) < m(Q) + \varepsilon\). Then \(E_{0} \cup E_{0} + d = E_{0} \cup E_{0} + d\), so \(m(E_{0} \cup E_{0} + d) = 2m(E_{0}) \geq 2(1 - \varepsilon)m(Q)\). Since \(E_{0} \cup E_{0} + d \subseteq Q \cup Q + d\), we also have \(m(E_{0} \cup E + d) < m(Q) + \varepsilon\). But then \(2(1 - \varepsilon)m(Q) \leq m(E_{0} \cup E_{0} + d) < m(Q) + \varepsilon\) and taking \(\varepsilon \to 0\) yields \(2m(Q) < m(Q)\). So \(E_{0} - E_{0} \subseteq E - E\) must contain an open ball around \(0\).  
③ Fix \(x\) and let \(L = \limsup_{y \to x} f(y) = \limsup_{\delta \to 0} \sup_{y \in B_{\delta}(x)} f(y)\). Then consider \(S_{\alpha} = \{x \in \mathbb{R}^{n} | f(x) \leq \alpha\}\), we will show every \(x \in S_{\alpha}\) has a ball \(B_{\delta}(x) \leq S_{\alpha}\), making \(S_{\alpha}\) open, and since \(\alpha\) is arbitrary, this will show \(f\) is Borel measurable. Let \(x \in S_{\alpha}\), so \(f(x) < \alpha\). Then since \(f\) is upper-semicts, pick \(\delta\) s.t. \(y \in B_{\delta}(x) \Rightarrow f(y) \leq f(x)\). But then \(y \in B_{\delta}(x) \Rightarrow f(y) \leq f(x) < \alpha \Rightarrow y \in S_{\alpha}\), so \(B_{\delta}(x) \leq S_{\alpha}\) as desired.  
④ \(S = \{x \in \mathbb{R}^{n} | \lim f_n(x) exists\} \in M\) iff \(S^c \in M\), which is what we'll show. Noting that if we let \(F(x) = \limsup_{n \to \infty} f_n(x)\), \(G(x) = \liminf_{n \to \infty} f_n(x)\), then \(S^c = \{x | F(x) > G(x)\}\)  
\(= U_{q \in Q}\{x | F(x) > q > G(x)\}\)  
\(= U_{q \in Q}\{\{x | F(x) > q\} \cap \{x | G(x) < q\}\)

<!-- page 43 -->

$$= \bigcup_{q \in \mathbb{Q}} (M_q \cap N_q) \text{ where each } M_q, N_q \text{ is measurable, thus making } S^c \text{ a countable union of measurable sets } \& \text{ thus measurable. (Eg, } M_q \text{ is measurable exactly because if } \{f_n\} \text{ are measurable, then } \limsup_{n \to \infty} f_n := F \text{ is measurable, as shown in class.)}$$

5a $f$ is well-defined because each $x \in C$ has a unique ternary expansion which contains no $1^n$, and $f$ is cts as we can write $g_n(x) = \underbrace{(a_1/2) \cdot (\frac{1}{2})^n}_{cts}$, so $f = \sum_{n=1}^{\infty} g_n$, where we have $|g_n(x)| \le 1/2^{n+1}$ which is summable, so $f$ is uniformly cts by the $M$-test. Moreover, $(0)_{10} = (0)_3 = (0.000 \dots)_3 \xrightarrow{f} (0.000 \dots)_2 = (0)_{10}$, so $f(0) = 0$, and $(1)_{10} = (0.222 \dots)_3 \xrightarrow{f} (0.111 \dots)_2 = (1)_{10}$, so $f(1) = 1$.

5b $f \to [0, 1]$, so consider $f^1(N)$ for $N$ the non-measurable set. Since this is a subset of a measure zero set, it is measurable, and so $\underbrace{f^1(N)}_{\text{measurable}} \xrightarrow{f} \underbrace{N}_{\text{cts}}$ not measurable.

6a Since $f$ is cts, constant fns are cts, and $f$ is a piecewise combination of cts fns that agree on intersections, $F$ is cts. Constant fns are nondecreasing, so it only remains to show $f$ is nondecreasing on $C$. Let $x = \sum a_n \bar{3}^n$, $y = \sum b_n \bar{3}^n$, and $x > y$. Then there is some minimal $N$ such that $a_k = b_k \forall k < N$ and $a_N > b_N$. Then $\frac{1}{2}a_N > \frac{1}{2}b_N$, and $\frac{1}{2}a_k = \frac{1}{2}b_k \forall k < N$, which means that $f(x) > f(y)$ since
$$f(x) - f(y) = \sum_{n=1}^{\infty} (\frac{1}{2}a_n - \frac{1}{2}b_n) \bar{2}^n = \frac{1}{2}(a_N - b_N) \bar{2}^N + \frac{1}{2} \sum_{n=N+1}^{\infty} (a_n - b_n) \bar{2}^n \ge \frac{1}{2}(a_N - b_N) \bar{2}^N > 0.$$ 

6b Since $F(x)$ and $x \mapsto x$ are continuous and nondecreasing, and in fact $x \mapsto x$ is strictly increasing, $G$ is continuous and strictly increasing & thus injective. To see that $G$ is surjective, we just note that $G(0)=0$ and $G(1)=2$, so this follows from the IVT.

6c1 Let $I$ be one of the intervals in $C^c$, then $x, y \in I \Rightarrow F(x) = F(y)$ and so $G(b) - G(a) = b - a = m(I)$. Then $m(I) = m(G(I))$ since $G$ is cts, and so $m(G(C^c)) = m(G(\bigcup_{n=1}^{\infty} I_n)) = m(\bigcup_{n=1}^{\infty} I_n) = 1$, so $m(G(C)) = m([0, 2] \setminus G(C^c)) = 2 - 1 = 1$.

6c2 We have $\mathbb{R} = \bigsqcup_{q \in \mathbb{Q}} (N + q)$, so $G(C) = \bigsqcup_{q \in \mathbb{Q}} (G(C) \cap N + q)$, so $m(G(C)) \le \sum_{i=1}^{\infty} (G(C) \cap N + q_i)$. $0 < 1 = m(G(C)) = \sum_{i=1}^{\infty} m(G(C) \cap N + q_i)$.

<!-- page 44 -->

Not every term can have $m_*(E_i)=0$, so some $E_i$ has $m(E_i)>0$. But then $E_i$ can not be

be measurable, since if we let $E_i = G(C) \cap \mathcal{N} + q_i$, then $x, y \in E_i \Rightarrow x - y \in \mathbb{R}^\backslash \mathbb{Q}$

so $E_i - E_i$ can't contain any ball around zero and thus $E$ can't be Lebesgue measurable by (2b).

Since $E_i \subseteq G(C)$ is a nonmeasurable set, we're done.

6c3 Let $\mathcal{N}' = E_i$, then $\mathcal{N}' = G(C) \cap \mathcal{N} + q_i$ for some $i$, so $G''(\mathcal{N}') \subseteq C$ and $m(C) = 0$ implies $G''(\mathcal{N}')$ is measurable and $m(G''(\mathcal{N}')) = 0$. But every cts function is Borel measurable, and since $G(G''(\mathcal{N}')) = \mathcal{N}'$ is not Borel, it can not pull back to a Borel set.

6d As shown above, $E_i$ is not measurable and $G''(E_i)$ is null, so take $\mathcal{Q} = \mathcal{X}_{G''(E_i)}$. Then

$$S_\alpha = \{ x \in [0,1] \mid \mathcal{Q}(x) > \alpha \} = \begin{cases} G''(E_i), & 0 \le \alpha < 1 \\ [0,1], & \alpha = 0 \\ \emptyset, & \text{else} \end{cases} \text{ both of which are measurable, so } \mathcal{Q} \in \mathcal{M}.$$

But for $\alpha = \frac{1}{2}$, $S_{\frac{1}{2}} = \{ x \in [0,2] \mid (\mathcal{Q} \circ G'')(x) > \frac{1}{2} \} = \{ x \in [0,2] \mid G''(x) \in G''(E_i) \} = E_i \in \mathcal{M}$.

<!-- page 45 -->

# Analysis HW #4

Zack Garza

1a) Let $f_k$ be the following function:

![img-1.jpeg](img-1.jpeg)

Note that this yields a triangle of area $\frac{1}{2}bh = \frac{1}{2}(k + \frac{1}{2}^{k+1} - k) \cdot 1 = 2^{-k}$, so we have $\int_R f_k = \int_k^{k+\frac{1}{2}^{k+1}} f_k = 2^{-k}$. Moreover, $k \neq j \Rightarrow [k, k+\frac{1}{2}^{k+1}] \cap [j, j+\frac{1}{2}^{j+1}] = \emptyset$, so let $g_N = \sum_{k=0}^N f_k$ and $g = \lim_{N \to \infty} g_N = \sum_{k=0}^\infty f_k$. Then $g_N \nearrow g$, so we can apply the MCT to obtain

$$\int_R g = \int_R \lim_{N \to \infty} g_N \stackrel{\text{MCT}}{=} \lim_{N \to \infty} \int_R g_N = \lim_{N \to \infty} \int_R \sum_{k=0}^N f_k = \lim_{N \to \infty} \sum_{k=0}^N \int_R f_k = \lim_{N \to \infty} \sum_{k=0}^N 2^{-k} = 1$$

However, $\limsup_{x \to \infty} g(x) = 1 > 0$, so $\lim_{x \to \infty} g(x) \neq 0$.

1b) Towards a contradiction, suppose $f \in L^+$ is uniformly cts and $\limsup_{x \to \infty} f(x) = \varepsilon > 0$. Choose a sequence $\{x_n\} \nearrow \infty$ such that for all $i, j$ we have $|x_i - x_j| > 1$. Then, for any $\delta < 1$ and any $x_i, x_j$, we have $B_\delta(x_i) \cap B_\delta(x_j) = \emptyset$. Now by uniform continuity of $f$, choose $\delta$ such that $\delta < 1$ and

$$y \in B_\delta(x) \Rightarrow |f(x) - f(y)| < \varepsilon \quad \forall x, y \in \mathbb{R}^N$$

Now let $n$ be fixed, and consider some $x \in B_\delta(x_n)$. We have $|f(x) - f(x_n)| < \varepsilon$; note that $|f(x_n)| > 0$ for all $n$ large enough; otherwise the limsup would be zero. It also must be the case that $|f(x)| > \varepsilon$;

otherwise $|f(x)| < \varepsilon \Rightarrow |f(x_n)| - |f(x)| > |0 - \varepsilon| = \varepsilon$, so

$$\varepsilon < |f(x_n)| - |f(x)| \leq |f(x_n) - f(x)| < \varepsilon$$

So $|f(x)| > \varepsilon$. But then

$$\int_{B_\delta(x_n)} |f| \geq \int_{B_\delta(x_n)} \varepsilon = \varepsilon \cdot m(B_\delta(x_n)) = \varepsilon \cdot 2\delta,$$

<!-- page 46 -->

and so if we let

$$X = \bigsqcup_{n=1}^{\infty} B_{S(x_n)} \subseteq \mathbb{R}^n,$$

we have

$$\int_{\mathbb{R}^n} |f| \ge \int_X |f| = \sum_{n=1}^{\infty} \int_{B_{S(n)}} |f| \le \sum_{n=1}^{\infty} \varepsilon \cdot 2\delta \longrightarrow \infty,$$

contradicting $f \in L'$.

2a) Let $X = \{x \in \mathbb{R}^n \mid |f(x)| = \infty\}$, then $X \cap X^c = \emptyset$ and $\mathbb{R}^n = X \sqcup X^c$, so

$$\int_{\mathbb{R}^n} |f| = \int_X |f| + \int_{X^c} |f| = \infty \cdot m(X) + \int_{X^c} |f| < \infty$$

since $f \in L'$, but if $m(X) > 0$ this yields a contradiction. So we must have $m(X) = 0$.
2b) We'll use the fact that $A \subseteq B$ and $\int_B |f| < \infty$, then $\int_B |f| - \int_A |f| = \int_{B \setminus A} |f|$. Noting that

$$\int_E |f| > \left( \int_{\mathbb{R}^n} |f| \right) - \varepsilon \iff \int_{\mathbb{R}^n} |f| - \int_E |f| < \varepsilon \iff \int_{E^c} |f| < \varepsilon,$$

we will produce an E st. $E^c$ satisfies this condition. Write $\mathbb{R}^n = \lim_{k \to \infty} B(k, \vec{o})$, the n-ball of radius k centered at $\vec{o} \in \mathbb{R}^n$. Since the map $(A \mapsto \int_A |f|)$ is a measure, it satisfies continuity from below, and since $B(k, \vec{o}) \ne \mathbb{R}^n$, we have $\lim_{k \to \infty} \int_{B(k, \vec{o})} |f| = \int_{\mathbb{R}^n} |f|$. Since this limit exists, let $\varepsilon > 0$ and choose N such that

$$\int_{\mathbb{R}^n} |f| - \int_{B(k, \vec{o})} |f| < \varepsilon \implies \varepsilon > \int_{\mathbb{R}^n} |f| - \int_{B(k, \vec{o})} |f| = \int_{B(k, \vec{o})^2} |f|,$$

so $E := B(N, \vec{o})$ satisfies the desired property.

③ We want to show a iff b iff c, where

a) $\int f < \infty$

b) $\sum_{k \in \mathbb{Z}} 2^k m(E_k) < \infty, \quad E_k = \{x \mid f(x) > 2^k\}$

c) $\sum_{k \in \mathbb{Z}} 2^k m(F_k) < \infty, \quad F_k = \{x \mid 2^k < f(x) \le 2^{k+1}\}$

Note that $F_i \cap F_j = \emptyset$ if $i \neq j$, and $F_k = E_k \setminus E_{k+1}$

<!-- page 47 -->

(b) iff (c): We have

$$\begin{array}{l} \sum_{k \geq 2^k} 2^k m(F_k) = \sum_{k \geq 2^k} [m(E_k) - m(E_{k+1})] \\ = \sum_{k \geq 2^k} 2^k m(E_k) - \sum_{k \geq 2^k} 2^k m(E_{k+1}) \\ = \sum_{k \geq 2^k} 2^k m(E_k) - \frac{1}{2} \sum_{k \geq 2^k} 2^k m(E_k) \\ = \sum_{k \geq 2^k} (1 - \frac{1}{2}) 2^k m(E_k) \\ = \frac{1}{2} \sum_{k \geq 2^k} 2^k m(E_k), \end{array}$$

Might need to use

absolute convergence

of these sums for

this to work.

and so either sum is finite iff the other is.

(a) $\Rightarrow$ (c) and (b) $\Rightarrow$ (a):

Write $X := \{x \mid f(x) > 0\} = \bigsqcup_{k \geq 2^k} F_k$, then $\int_X f = \sum_{k \geq 2^k} \int_{F_k} f$ and we have

$$\sum_{k \geq 2^k} 2^k m(F_k) \leq \sum_{k \geq 2^k} \int_{F_k} f \leq \sum_{k \geq 2^k} 2^{k+1} m(F_k) = \sum_{k \geq 2^k} 2^k m(E_k)$$

So

$$\int_X f < \infty \Rightarrow \sum_{k \geq 2^k} 2^k m(F_k) < \infty$$

and

$$\sum_{k \geq 2^k} 2^k m(E_k) < \infty \Rightarrow \int_X f < \infty.$$

4) Let $A_k = \{x \in \mathbb{R}^n \mid 2^k < \|x\| \leq 2^{k+1}\}$, so we have

$$A := \{x \in \mathbb{R}^n \mid \|x\| \leq 1\} = \bigsqcup_{k=1}^\infty A_{-k}$$

$$B := \{x \in \mathbb{R}^n \mid \|x\| > 1\} = \bigsqcup_{k=0}^\infty A_k$$

$$\omega_n 2^{n^k} \leq m(A_k) \leq \omega_n 2^{n^{(k+1)}}, \quad \omega_n 2^{-n^k} \leq m(A_{(-k)}) \leq \omega_n 2^{-n^{(k-1)}}$$

Volume of unit n-ball.

Then noting that

$$x \in A_k \Rightarrow 2^k < \|x\| \leq 2^{k+1} \Rightarrow 2^{-p^{(k+1)}} \leq \|x\|^p < 2^{-kp},$$

$$x \in A_{(-k)} \Rightarrow 2^{-k} < \|x\| \leq 2^{-(k-1)} \Rightarrow 2^{p^{(k-1)}} \leq \|x\|^p < 2^{pk}$$

we define

Raised to -p power for p > 0.

<!-- page 48 -->

(4a)

$$I_A = \int_A \|\vec{x}\|^p, \quad I_B = \int_B \|\vec{x}\|^p$$

and find

$$I_A \le \sum_{k=1}^{\infty} 2^{p^k} m(A_{t-k}) \le \sum_{k=1}^{\infty} 2^{p^k} 2^{-n(k-1)} = \omega_n \sum_{k=1}^{\infty} (2^{-k})^{n-p} < \infty \quad \text{iff } p < n,$$

$$\text{and } \infty > I_A \ge \sum_{k=1}^{\infty} 2^{p^{(k-1)}} m(A_{t-k}) \ge \sum_{k=1}^{\infty} 2^{p^{(k-1)}} \omega_n 2^{-k} = \omega_n 2^p \sum_{k=1}^{\infty} (2^{-k})^{n-p} \quad \text{iff } p < n$$

(4b)

Similarly

$$I_B \le \sum_{k=0}^{\infty} 2^{-kp} \omega_n 2^{n(k+1)} = \omega_n 2^n \sum_{k=0}^{\infty} (2^{-k})^{p-n} < \infty \quad \text{iff } p > n,$$

$$\text{and } \infty > I_B \ge \sum_{k=0}^{\infty} 2^{-p^{(k+1)}} \omega_n 2^{nk} = \omega_n 2^p \sum_{k=0}^{\infty} (2^{-k})^{p-n} \quad \text{iff } p > n.$$

![img-2.jpeg](img-2.jpeg)

⑤ To see that $\hat{f}$ is bounded, supposing that $f \in L^1(\mathbb{R}^n)$, we have

$$|\hat{f}(\xi)| \le \int |f(x)| \cdot \left| \frac{e^{2\pi i x \cdot \xi}}{\xi} \right| \le \int_{\mathbb{R}^n} |f| < \infty.$$

To see that it is cts, we will use the sequential defn. of continuity.

So let $\{\xi_n\} \to \xi$ be any sequence converging to $\xi$. Then

$$\begin{aligned} \lim_{n \to \infty} |\hat{f}(\xi_n) - \hat{f}(\xi)| &= \lim_{n \to \infty} \left| \int f(x) [e^{2\pi i x \cdot \xi_n} - e^{2\pi i x \cdot \xi}] \right| \\ &= \lim_{n \to \infty} \left| \int f(x) e^{2\pi i x \cdot \xi} [e^{2\pi i x \cdot (\xi_n - \xi)} - 1] \right| \\ &\le \lim_{n \to \infty} \int |f(x) e^{2\pi i x \cdot \xi}| \cdot |e^{2\pi i x \cdot (\xi_n - \xi)} - 1| \end{aligned}$$

<!-- page 49 -->

$$\begin{array}{l} DCT = \int \lim_{n \to \infty} |f(x) e^{2\pi i x \cdot \xi} | \cdot |e^{2\pi i x \cdot (\xi_n - \xi)} - 1| \\ = \int \underbrace{|f(x) e^{2\pi i x \cdot \xi}|}_{\text{no n involved}} \cdot \lim_{n \to \infty} |e^{2\pi i x \cdot (\xi_n - \xi)} - 1| \\ = \int |f(x) e^{2\pi i x \cdot \xi}| \cdot 0 \\ = 0 \end{array}$$

Where the DCT can be applied by letting

$$\begin{array}{l} f_n = f(x) e^{2\pi i x \cdot \xi} \left( e^{2\pi i x \cdot (\xi_n - \xi)} - 1 \right) \\ \Rightarrow |f_n| = |f(x) e^{2\pi i x \cdot \xi}| \cdot |e^{2\pi i x \cdot (\xi_n - \xi)} - 1| \\ \leq |f(x) e^{2\pi i x \cdot \xi}| \cdot \left( \underbrace{|e^{2\pi i x \cdot (\xi_n - \xi)}|}_{\leq 1} + |-1| \right) \\ \leq |f(x) e^{2\pi i x \cdot \xi}| \cdot 2 \\ \leq 2 |f| \in L'. \end{array}$$

But this says $\lim_{n \to \infty} |\hat{f}(\xi_n) - \hat{f}(\xi)| = 0$, so $\hat{f}$ is continuous.

(a.i.) Let $g_n = |f_n| - |f_n - f|$; then $g_n \to |f|$ and

$$|g_n| = ||f_n| - |f_n - f|| \leq |f_n - (f_n - f)| = |f| \in L',$$

Reverse $\Delta$-ineq

so $\lim_{n \to \infty} \int g_n = \int \lim_{n \to \infty} g_n = \int |f| = B$ by the DCT. We can then write

$$\begin{array}{l} \lim_{n \to \infty} \int |f_n - f| = \lim_{n \to \infty} \int |f_n - f| - |f_n| + |f_n| \\ = \lim_{n \to \infty} \int |f_n| - \underbrace{(|f_n| - |f_n - f|)}_{:= g_n} \\ = \lim_{n \to \infty} \int |f_n| - g_n \\ = \lim_{n \to \infty} \int |f_n| - \lim_{n \to \infty} \int g_n = A - B \end{array}$$

Since

<!-- page 50 -->

6a.ii) Let $f_n = n \cdot \chi_{(0, \tilde{n})}$, then $f_n \to 0 := f_{a.e.}$, so $\int f = \int 0 = 0 \Rightarrow B = 0$, but $\int f_n = 1$ for all $n$, so $\lim_{n \to \infty} \int |f_n| = 1 = A \neq B$.
6b) ($\Rightarrow$) $\lim_{k \to \infty} \int |f_k - f| = 0 = A - B \Rightarrow A = B \Rightarrow \lim_{k \to \infty} \int |f_k| = \int |f|$.
($\Leftarrow$) $\lim_{k \to \infty} \int |f_k| = \int |f| \Rightarrow A = B \Rightarrow A - B = 0 \Rightarrow \int |f_k - f| = A - B = 0$.
7a) Let $\{t_n\} \to t$ and define $g_n(x) = f(x) \left( \frac{\cos(t_n x) - \cos(tx)}{t_n - t} \right)$.
Then $\lim_{n \to \infty} g_n(x) = f(x) \text{ ?/} t(\cos(tx)) = f(x) \times \sin(tx)$, and applying the Mean Value Theorem, we have $\frac{\cos(t_n x) - \cos(tx)}{t_n - t} = x \sin(tx) \bigg|_{x=\xi} = \xi \sin(t\xi)$ for some $\xi$, so $|g_n| = |f(x) \times \sin(tx)| = |f(x) \xi \sin(t\xi)| \leq \xi |f| \in L^1$,
so $\lim_{n \to \infty} \int g_n \overset{DCT}{=} \int \lim_{n \to \infty} g_n = \int g = \int f(x) \times \sin(tx) \, dx$, which is integrable because $\int |f(x) \times \sin(tx)| \leq \int |xf(x)| < \infty$ since $xf \in L^1$.
Thus $F'(t) = \int_R f(x) \times \sin(tx) \, dx$.
7b) $\lim_{t \to 0} \int_0^t \frac{e^{t\sqrt{x}} - 1}{t} \, dx = \lim_{t \to 0} \int_0^t \frac{e^{t\sqrt{x}} - e^{0\sqrt{x}}}{t - 0} \, dx \overset{DCT}{=} \int_0^t \lim_{t \to 0} \left( \frac{e^{t\sqrt{x}} - e^{0\sqrt{x}}}{t - 0} \right) dx$
$\therefore \int_0^t \frac{\partial}{\partial t} e^{t\sqrt{x}} \bigg|_{t=0} dx = \int_0^t \sqrt{x'} e^{t\sqrt{x'}} \bigg|_{t=0} dx = \int_0^t \sqrt{x'} \, dx = (\frac{2}{3})x^{3/2} \bigg|_0^t = 2/3$.
The DCT here is justified by letting $\{t_n\} \to 0$ and setting $g_n(t) = \frac{e^{t\sqrt{x}} - e^{t_n\sqrt{x}}}{t - t_n}$.
Then by the MVT, for each $n$ we have $g_n(t) = \text{?}/t e^{t\sqrt{x}} \bigg|_{t=c}$ for some $c \in [0, t_n] \leq [0, 1]$.
But $\text{?}/t e^{t\sqrt{x}} \bigg|_{t=c} = \sqrt{x'} e^{t\sqrt{x'}} \bigg|_{t=c} = \sqrt{x'} e^{c\sqrt{x'}} \leq \sqrt{1} e^{c\sqrt{1}} = e^c \leq e^1$, so $|g_n| \leq e^1 \in L^1([0, 1])$,
since $\int_0^t e \, dx = e < \infty$, so $f(x) = e$ is a dominating function.

<!-- page 51 -->

# Problem Set 5

D. Zack Garza

October 23, 2019

## Contents

|  **1** | **Problem 1** | **1**  |
| --- | --- | --- |
|  **2** | **Problem 2** | **3**  |
|  **3** | **Problem 3** | **4**  |
|  **4** | **Problem 4** | **4**  |
|  4.1 | Part (a) | 4  |
|  4.2 | Part (b) | 6  |
|  **5** | **Problem 5** | **6**  |
|  **6** | **Problem 6** | **7**  |
|  6.1 | Part (a) | 7  |
|  6.2 | Part (b) | 8  |

## 1 Problem 1

We first make the following claim:

$$S := \sum_{j=1}^\infty \sum_{k=1}^\infty a_{jk} = \sup \left\{ \sum_{(j,k) \in B} a_{jk} \ni B \subset \mathbb{N}^2, \ |B| < \infty \right\}$$
$$T := \sum_{k=1}^\infty \sum_{j=1}^\infty a_{kj} = \sup \left\{ \sum_{(j,k) \in C} a_{kj} \ni C \subset \mathbb{N}^2, \ |B| < \infty \right\}.$$

It suffices to show the first equality holds, as the other case will follow similarly. Let $S = \sum_{j=1}^\infty \sum_{k=1}^\infty a_{jk}$ and $S' = \sup \left\{ \sum_{(j,k) \in B} a_{jk} \ni B \subset \mathbb{N}^2, \ |B| < \infty \right\}$.

Then consider any bounded set $B \subset \mathbb{N}^2$; so $B \subset \{1, \cdots, n_1\} \times \{1, \cdots, n_2\}$ for some $n_1, n_2 \in \mathbb{N}$. We then have

1

<!-- page 52 -->

$$\sum_{B} a_{jk} \leq \sum_{j=1}^{n_1} \sum_{k=1}^{n_2} a_{jk} \leq \sum_{j=1}^{\infty} \sum_{k=1}^{\infty} a_{jk}.$$

where the first equality holds $a + jk \geq 0$ for all $j, k$, so the sum can only increase if we add more terms. But this holds for every $B$ and thus holds if we take the supremum over all of them, so $S' \leq S$.

To see that $S \leq S'$, we can just note that

$$\begin{aligned} S &= \lim_{J \to \infty} \sum_{j=1}^{J} \left( \lim_{K \to \infty} \sum_{k=1}^{K} a_{jk} \right) \\ &= \lim_{J \to \infty} \lim_{K \to \infty} \sum_{j=1}^{J} \sum_{k=1}^{K} a_{jk} \\ &\leq \lim_{J \to \infty} \lim_{K \to \infty} S' \\ &= S', \end{aligned}$$

where the limits commute with finite sums, and we the sum can be replaced with $S'$ because the set $\{1, \cdots, K\} \times \{1, \cdots J\}$ is one of the finite sets over which the supremum is taken. Moreover, $S'$ is a number that doesn't depend on $J, K$, yielding the final equality. $\square$

We will show that $S = T$ by showing that $S \leq T$ and $T \leq S$.

Let $B \subset \mathbb{N}^2$ be finite, so $B \subseteq [0, I] \times [0, J] \subset \mathbb{N}^2$.

Now letting $R > \max(I, J)$, we can define $C = [0, R]^2$, which satisfies $B \subseteq C \subset \mathbb{N}^2$ and $|C| < \infty$.

Moreover, since $a_{jk} \geq 0$ for all pairs $(j, k)$, we have the following inequality:

$$\sum_{(j,k) \in B} a_{jk} < \sum_{(k,j) \in C} a_{jk} \leq \sum_{(k,j) \in C} a_{jk} \leq T,$$

since $T$ is a supremum over all such sets $C$, and the terms of any finite sum can be rearranged.

But since this holds for every $B$, we this inequality also holds for the supremum of the smaller term by order-limit laws, and so

$$S := \sup_{B} \sum_{(k,j) \in B} a_{jk} \leq T.$$

(Use epsilon-delta argument)

An identical argument shows that $T \leq S$, yielding the desired equality. $\square$

<!-- page 53 -->

## 2 Problem 2

We want to show the following equality:

$$\int_{0}^{1} g(x) \, dx = \int_{0}^{1} f(x) \, dx.$$

To that end, we can rewrite this using the integral definition of $g(x)$:

$$\int_{0}^{1} \int_{x}^{1} \frac{f(t)}{t} \, dt \, dx = \int_{0}^{1} f(x) \, dx$$

Note that if we can switch the order of integration, we would have

$$\begin{aligned} \int_{0}^{1} \int_{x}^{1} \frac{f(t)}{t} \, dt \, dx = &? \int_{0}^{1} \int_{0}^{t} \frac{f(t)}{t} \, dx \, dt \\ &= \int_{0}^{1} \frac{f(t)}{t} \int_{0}^{t} dx \, dt \\ &= \int_{0}^{1} \frac{f(t)}{t} (t - 0) \, dt \\ &= \int_{0}^{1} f(t) \, dt, \end{aligned}$$

which is what we wanted to show, and so we are simply left with the task of showing that this is switch of integrals is justified.

To this end, define

$$F : \mathbb{R}^2 \to \mathbb{R}$$

$$(x, t) \mapsto \frac{\chi_A(x, t) \hat{f}(x, t)}{t}.$$

where $A = \{(x, t) \subset \mathbb{R}^2 \ni 0 \le x \le t \le 1\}$ and $\hat{f}(x, t) := f(t)$ is the cylinder on $f$.

This defines a measurable function on $\mathbb{R}^2$, since characteristic functions are measurable, the cylinder over a measurable function is measurable, and products/quotients of measurable functions are measurable.

In particular, $|F|$ is measurable and non-negative, and so we can apply Tonelli to $|F|$. This allows us to write

$$\begin{aligned} \int_{\mathbb{R}^2} |F| &= \int_{0}^{1} \int_{0}^{t} \left| \frac{f(t)}{t} \right| \, dx \, dt \\ &= \int_{0}^{1} \int_{0}^{t} \frac{|f(t)|}{t} \, dx \, dt \quad \text{since } t > 0 \\ &= \int_{0}^{1} \frac{|f(t)|}{t} \int_{0}^{t} dx \, dt \\ &= \int_{0}^{1} |f(t)| < \infty, \end{aligned}$$

<!-- page 54 -->

where the switch is justified by Tonelli and the last inequality holds because $f$ was assumed to be measurable.

Since this shows that $F \in L^{1}(\mathbb{R}^{2})$, and we can thus apply Fubini to $F$ to justify the initial switch. $\square$

### 3 Problem 3

Let $A = \{0 \leq x \leq y\} \subset \mathbb{R}^{2}$, and define

$$f(x, y) = \frac{x^{1/3}}{(1 + xy)^{3/2}}$$

$$F(x, y) = \chi_{A}(x, y)f(x, y).$$

Note that $F$ Then, if all iterated integrals exist and a switch of integration order is justified, we would have

$$\begin{array}{l} \int_{\mathbb{R}^{2}} F = ? \int_{0}^{\infty} \int_{y}^{\infty} f(x, y) \, dx \, dy \\ = ? \int_{0}^{\infty} \int_{x}^{\infty} \frac{x^{1/3}}{(1 + xy)^{3/2}} \, dy \, dx \\ = 2 \int_{\mathbb{R}} \frac{1}{x^{2/3}\sqrt{1 + x^{2}}} \, dx \\ = 2 \int_{0}^{1} \frac{1}{x^{2/3}\sqrt{1 + x^{2}}} \, dx + 2 \int_{1}^{\infty} \frac{1}{x^{2/3}\sqrt{1 + x^{2}}} \, dx \\ \leq \int_{0}^{1} x^{-2/3} \, dx + \int_{0}^{\infty} x^{-5/3} \\ = 2(3) + 2\left(\frac{3}{2}\right) < \infty, \end{array}$$

where the first term in the split integral is bounded by using the fact that $\sqrt{1 + x^{2}} \geq \sqrt{x^{2}} = x$, and the second term from $x > 1 \implies x > 0 \implies \sqrt{1 + x^{2}} \geq \sqrt{1}$.

Since $F$ is non-negative, we have $|F| = F$, and so the above computation would imply that $F \in L^{1}(\mathbb{R}^{2})$. It thus remains to show that $\int F$ is equal to its iterated integrals, and that the switch of integration order is justified

Since $F$ is non-negative, Tonelli can be applied directly if $F$ is measurable in $\mathbb{R}^{2}$. But $f$ is measurable on $A$, since it is continuous at almost every point in $A$, and $\chi_{A}$ is measurable, so $F$ is a product of measurable functions and thus measurable.

### 4 Problem 4

#### 4.1 Part (a)

For any $x \in \mathbb{R}^{n}$, let $A_{x} := A \cap (x - B)$.

<!-- page 55 -->

We can then write $A_t := A \cap (t - B)$ and $A_s := A \cap (s - B)$, and thus

$$\begin{array}{l} g(t) - g(s) = m(A_t) - m(A_s) \\ = \int_{\mathbb{R}^n} \chi_{A_t}(x) \, dx - \int_{\mathbb{R}^n} \chi_{A_s}(x) \, dx \\ = \int_{\mathbb{R}^n} \chi_{A_t}(x) - \chi_{A_s}(x) \, dx \\ = \int_{\mathbb{R}^n} \chi_{A_t}(x) - \chi_{A_t}(t - s + x) \, dx \\ \quad (\text{since } x \in s - B \iff s - x \in B \iff t - (s - x) \in t - B), \end{array}$$

and thus by continuity in $L^1$, we have

$$|g(t) - g(s)| \leq \int_{\mathbb{R}^n} |\chi_{A_t}(x) - \chi_{A_t}(t - s + x)| \, dx \to 0 \quad \text{as} \quad t \to s$$

which means $g$ is continuous.

To see that $\int g = m(A)m(B)$, if an interchange of integrals is justified, we can write

$$\begin{array}{l} \int_{\mathbb{R}^n} g(t) \, dt = \int_{\mathbb{R}^n} \int_{\mathbb{R}^n} \chi_{A_t}(x) \, dx \, dt \\ = \int_{\mathbb{R}^n} \int_{\mathbb{R}^n} \chi_A(x) \chi_{t-B}(x, t) \, dx \, dt \\ = \int_{\mathbb{R}^n} \int_{\mathbb{R}^n} \chi_A(x) \chi_{t-B}(x, t) \, dx \, dt \\ = \int_{\mathbb{R}^n} \int_{\mathbb{R}^n} \chi_A(x) \chi_B(t - x) \, dx \, dt \\ \quad (\text{since } x \in t - B \iff t - x \in B) \\ = ? \int_{\mathbb{R}^n} \int_{\mathbb{R}^n} \chi_A(x) \chi_B(t - x) \, \mathbf{dt} \, \mathbf{dx} \\ = \int_{\mathbb{R}^n} \chi_A(x) \int_{\mathbb{R}^n} \chi_B(t - x) \, dt \, dx \\ = \int_{\mathbb{R}^n} \chi_A(x) \, m(B) \, dt \\ \quad (\text{by translation invariance of Lebesgue integral}) \\ = m(B) \int_{\mathbb{R}^n} \chi_A \, dt \\ = m(B)m(A). \end{array}$$

To see that this is justified, we note that that the map $F(x, t) = \chi_A(x) \chi_B(x - t)$ is non-negative, and we claim is measurable in $\mathbb{R}^{2n}$.

- The first component is $\chi_A(x)$, which is measurable on $\mathbb{R}^n$, and thus the cylinder over it will be measurable on $\mathbb{R}^{2n}$.

<!-- page 56 -->

- The second component involves $\chi_B(t - x)$, which is $\chi_B(x)$ composed with a reflection (which is still measurable) followed by a translation (which is again still measurable).
- Thus, as a product of two measurable functions, the integrand is measurable.

So Tonelli applies to $|F|$, and thus $\int |F| = m(A)m(B) < \infty$ since $A, B$ were assumed to be bounded. But then $F$ is integrable by Fubini, and the claimed equality holds.

## 4.2 Part (b)

Supposing that $m(A), m(B) > 0$, we have $\int g(t) \, dt > 0$, using the fact that $\int g = 0$ a.e. $\iff g = 0$ a.e., we can conclude that if $T = \{t \ni g(t) \neq 0\}$, then $m(T) > 0$. So there is some $t \in \mathbb{R}^n$ such that $g(t) \neq 0$, and since $g$ is continuous, there is in fact some open ball $B_t$ containing $t$ such that $t' \in B_t \implies g(t') \neq 0$. So we have

- $\forall t' \in B_t, \ A \cap t' - B \neq \emptyset \iff$
- $\forall t' \in B_t, \ \exists x \in A \cap t' - B \iff$
- $\forall t' \in B_t, \ \exists x$ such that $x \in A$ and $x \in t' - B \iff$
- $\forall t' \in B_t, \ \exists x$ such that $x \in A$ and $x = t' - B$ for some $b \in B \iff$
- $\forall t' \in B_t, \ \exists x$ such that $x \in A$ and $t' = x + B$ for some $b \in B \iff$
- $\forall t' \in B_t, \ \exists t'$ such that $t' \in A + B$

And thus $B_t \subseteq A + B$.

## 5 Problem 5

If the iterated integrals exist and are equal (so an interchange of integration order is justified), we have

$$\begin{aligned} \int_0^1 F(x)g(x) &:= \int_0^1 \left( \int_0^x f(y) \, dy \right) g(x) \, dx \\ &= \int_0^1 \int_0^x f(y)g(x) \, dy \, dx \\ &= \int_0^1 \int_y^1 f(y)g(x) \, \mathbf{dx} \, \mathbf{dy} \\ &= \int_0^1 f(y) \left( \int_y^1 g(x) \, dx \right) \, dy \\ &= \int_0^1 f(y)(G(1) - G(y)) \, dy \\ &= G(1) \int_0^1 f(y) \, dy - \int_0^1 f(y)G(y) \, dy \\ &= G(1)(F(1) - F(0)) - \int_0^1 f(y)G(y) \, dy \\ &= G(1)F(1) - \int_0^1 f(y)G(y) \, dy \qquad \text{since } F(0) = 0, \end{aligned}$$

which is what we want to show.

<!-- page 57 -->

To see that this is justified, let $I = [0, 1]$ and note that the integrand can be written as $H(x, y) = \hat{f}(x, y)\hat{g}(x, y)$ where $\hat{f}(x, y) = \chi_I f(y)$ and $\hat{g}(x, y) = \chi_I g(x)$ are cylinders over $f$ and $g$ respectively. Since $f, g$ are in $L^1(I)$, their cylinders are measurable over $\mathbb{R} \times I$, and thus $\hat{f}, \hat{g}$ are measurable on $\mathbb{R}^2$ as products of measurable functions. Then $H$ is a measurable function as a product of measurable functions as well.

But then $|H|$ is non-negative and measurable, so by Tonelli all iterated integrals will be equal. We want to show that $H \in L^1(\mathbb{R}^2)$ in order to apply Fubini, so we will show that $\int |H| < \infty$.

To that end, noting that $f, g \in L^1$, we have $\int_0^1 f := C_f < \infty$ and $\int_0^1 g := C_g < \infty$. Then,

$$\begin{aligned} \int_{\mathbb{R}^2} |H| &= \int_0^1 \int_0^1 |f(x)g(y)| \, dx \, dy \\ &= \int_0^1 \int_0^1 |f(x)| \, |g(y)| \, dx \, dy \\ &= \int_0^1 |g(y)| \left( \int_0^1 |f(x)| \, dx \right) \, dy \\ &= \int_0^1 |g(y)| C_f \, dy \\ &= C_f \int_0^1 |g(y)| \, dy \\ &= C_f C_g < \infty, \end{aligned}$$

and thus by Fubini, the original interchange of integrals was justified.

## 6 Problem 6

### 6.1 Part (a)

We have

<!-- page 58 -->

$$\begin{array}{l} \int_{\mathbb{R}} |A_h(f)(x)| \, dx = \int_{\mathbb{R}} \left| \frac{1}{2h} \int_{x-h}^{x+h} f(y) \, dy \right| \, dx \\ = \frac{1}{2h} \int_{\mathbb{R}} \left| \int_{x-h}^{x+h} f(y) \, dy \right| \, dx \\ \leq \frac{1}{2h} \int_{\mathbb{R}} \left( \int_{x-h}^{x+h} |f(y)| \, dy \right) \, dx \\ = \frac{1}{2h} \int_{\mathbb{R}} \int_{x-h}^{x+h} |f(y)| \, dy \, dx \\ = ? \frac{1}{2h} \int_{\mathbb{R}} \int_{y-h}^{y+h} |f(y)| \, \mathbf{dx} \, \mathbf{dy} \\ = \frac{1}{2h} \int_{\mathbb{R}} |f(y)| \int_{y-h}^{y+h} \, dx \, dy \\ = \frac{1}{2h} \int_{\mathbb{R}} |f(y)| \, ((y+h) - (y-h)) \, dy \\ = \frac{1}{2h} \int_{\mathbb{R}} 2h |f(y)| \, dy \\ = \int_{\mathbb{R}} |f(y)| \, dy < \infty \end{array}$$

since $f$ was assumed to be in $L^1(\mathbb{R})$, where the changed bounds of integration are determined by considering the following diagram:

To justify the change in the order of integration, consider the function $H(x,y) = \frac{1}{2h} \chi_A(x,y) f(y)$ where $A = \{(x,y) \in \mathbb{R}^2 \ni -\infty < x - h \leq x, y \leq x + h\}$. Since $f$ is measurable, the constant function $(x,y) \mapsto \frac{1}{2h}$ is measurable, and characteristic functions are measurable, $H$ is a product of measurable functions and thus measurable.

Thus it makes sense to write $\int |H|$ as an iterated integral by Tonelli, and since $\int_{\mathbb{R}^2} |H| = \int_{\mathbb{R}} |A_h(f)| < \infty$ by the above calculation, we have $H \in L^1(\mathbb{R}^2)$, and Fubini applies.

## 6.2 Part (b)

Let $\varepsilon > 0$; we then have

<!-- page 59 -->

![img-3.jpeg](img-3.jpeg)

Figure 1: Changing the bounds of integration

\[
\begin{array}{l} \int_ {\mathbb {R}} | A _ {h} (f) (x) - f (x) | d x = \int_ {\mathbb {R}} \left| \left(\frac {1}{2 h} \int_ {B (h, x)} f (y) d y\right) - f (x) \right| d x \\ = \int_ {\mathbb {R}} \left| \left(\frac {1}{2 h} \int_ {B (h, x)} f (y) d y\right) - \frac {1}{2 h} \int_ {B (h, x)} f (x) d y \right| d x \\ \text { since } \frac {1}{2 h} \int_ {x - h} ^ {x + h} f (x) d y = \frac {1}{2 h} f (x) ((x + h) - (x - h)) = \frac {1}{2 h} f (x) 2 h = f (x) \\ = \int_ {\mathbb {R}} \left| \frac {1}{2 h} \int_ {B (h, x)} f (y) - f (x) d y \right| d x \\ \leq \int_ {\mathbb {R}} \frac {1}{2 h} \int_ {x - h} ^ {x + h} | f (y) - f (x) | d y d x \\ \leq \int_ {\mathbb {R}} \frac {1}{2 h} \int_ {- h} ^ {h} | f (y - x) - f (x) | d y d x \\ \end{array}
\]

but since \( h \to 0 \) will force \( y \to x \) in the integral, for a fixed \( x \) we can let \( \tau_x(y) = f(y - x) \) and we have \( \| \tau_x - f \|_1 \to 0 \) by continuity in \( L^1 \). Thus \( \int_{-h}^{h} |f(y - x) - f(x)| \to 0 \), forcing \( \| A_h(f) - f \|_1 \to 0 \) as \( h \to 0 \).

<!-- page 60 -->

# Assignment 6: The Fourier Transform

D. Zack Garza

November 5, 2019

## Contents

|  **1** | **Problem 1** | **1**  |
| --- | --- | --- |
|  **2** | **Problem 2** | **2**  |
|  2.1 | Part (a) | 2  |
|  2.2 | Part (b) | 3  |
|  2.2.1 | (i) | 3  |
|  2.2.2 | (ii) | 3  |
|  **3** | **Problem 3** | **4**  |
|  3.1 | (a) | 4  |
|  3.1.1 | (i) | 4  |
|  3.1.2 | (ii) | 4  |
|  3.2 | (b) | 4  |
|  **4** | **Problem 4** | **5**  |
|  4.1 | (a) | 5  |
|  4.1.1 | (i) | 5  |
|  4.1.2 | (ii) | 5  |
|  4.2 | (b) | 6  |
|  **5** | **Problem 5** | **7**  |
|  5.1 | (a) | 7  |
|  5.2 | (b) | 8  |
|  5.2.1 | (i) | 8  |
|  5.2.2 | (ii) | 8  |
|  5.3 | (c) | 8  |
|  **6** | **Problem 6** | **9**  |

## 1 Problem 1

Assuming the hint, we have

1

<!-- page 61 -->

$$\lim _ {| \xi | \to \infty} \hat {f} (\xi) = \lim _ {| \xi^ {\prime} | \to 0} \frac {1}{2} \int_ {\mathbb {R} ^ {n}} \left[ f (x)) - f (x - \xi^ {\prime}) \right] e ^ {- 2 \pi i x \cdot \xi} d x$$

The fact that the limit as $\xi \to \infty$ is equivalent to the limit $\xi' \to 0$ is a direct consequence of computing

$$\lim _ {| \xi | \to \infty} \frac {\xi}{2 | \xi | ^ {2}} = \lim _ {| \xi | \to \infty} \frac {1}{2 | \xi |} \frac {\xi}{| \xi |} = \mathbf {0},$$

since $\frac{\xi}{|\xi|}$ is a unit vector, and the term $\frac{1}{2|\xi|}$ is a scalar that goes to zero.

But as an immediate consequence, this yields

$$\begin{array}{l} \left| \hat {f} (\xi) \right| = \frac {1}{2} \left| \int_ {\mathbb {R} ^ {n}} \left[ f (x) - f (x - \xi^ {\prime}) \right] e ^ {- 2 \pi i x \cdot \xi} d x \right| \\ \leq \int_ {\mathbb {R} ^ {n}} | f (x) - f (x - \xi^ {\prime}) | \left| e ^ {- 2 \pi i x \cdot \xi} \right| d x \\ \leq \int_ {\mathbb {R} ^ {n}} | f (x) - f (x - \xi^ {\prime}) | d x \\ \rightarrow 0, \\ \end{array}$$

which follows from continuity in $L^1$ since $f(x - \xi') \to f(x)$ as $\xi' \to 0$.

It thus only remains to show that the hint holds.

Note: Sorry, I couldn't figure out how to prove the hint!!

## 2 Problem 2

### 2.1 Part (a)

Assuming an interchange of integrals is justified, we have

<!-- page 62 -->

$$\begin{array}{l} \widehat{f * g}(\xi) := \int \int f(x - y)g(y) \ e^{-2\pi i x \cdot \xi} \ dy \ dx \\ \quad = ? \int \int f(x - y)g(y) \ e^{-2\pi i x \cdot \xi} \ dx \ dy \\ \quad = \int \int f(t)e^{-2\pi i(x-y)\cdot\xi} \ g(y) \ e^{-2\pi i y \cdot \xi} \ dx \ dy \\ \quad \quad (t = x - y, \ dt = dx) \\ \quad = \int \int f(t)e^{-2\pi i t \cdot \xi}g(y)e^{-2\pi i y \cdot \xi} \ dt \ dy \\ \quad = \int f(t)e^{-2\pi i t \cdot \xi} \left(\int g(y) \ e^{-2\pi i y \cdot \xi} \ dy\right) \ dt \\ \quad = \int f(t)e^{-2\pi i t \cdot \xi} \ \hat{g}(\xi) \ dt \\ \quad = \hat{g}(\xi) \int f(t)e^{-2\pi i t \cdot \xi} \ dt \\ \quad = \hat{g}(\xi)\hat{f}(\xi). \end{array}$$

To see that this swap is justified, we'll apply Fubini-Tonelli. Note that if $f, g \in L^1(\mathbb{R}^n)$, then the map $(x, y) \mapsto f(x - y)$ is measurable on $\mathbb{R}^n \times \mathbb{R}^n$. Since $g$ is measurable as well, taking the cylinder on $g$ is also measurable on $\mathbb{R}^n \times \mathbb{R}^n$. The exponential is continuous, and thus measurable on $\mathbb{R}^n$. Thus the integrand $F(x, y)$ is a product of measurable functions and thus measurable. In particular, $|F| = |fg|$ is measurable, and the computation shows that one iterated integral is finite. From a previous homework question, we know that $f \in L^1 \implies \hat{f}$ is bounded, and thus $\hat{f}\hat{g}$ is bounded. Since $|F|$ is measurable and one iterated integrable was finite, Fubini-Tonelli applies.

## 2.2 Part (b)

We'll use the following lemma: if $\hat{f} = \hat{g}$, then $f = g$ almost everywhere.

### 2.2.1 (i)

By part 1, we have

$$\widehat{f * g} = \hat{f}\hat{g} = \hat{g}\hat{f} = \widehat{g * f},$$

and so by the lemma, $f * g = g * f$.

Similarly, we have

$$(\widehat{f * g}) * h = \widehat{f * g} \ \hat{h} = \hat{f} \ \hat{g} \ \hat{h} = \hat{f} \ \widehat{g * h} = f * (g * h).$$

### 2.2.2 (ii)

Suppose that there exists some $I \in L^1$ such that $f * I = f$. Then $\widehat{f * I} = \hat{f}$ by the lemma, so $\hat{f} \ \hat{I} = \hat{f}$ by the above result.

<!-- page 63 -->

But this says that $\hat{f}(\xi)\hat{I}(\xi) = \hat{f}(\xi)$ almost everywhere, and thus $\hat{I}(\xi) = 1$ almost everywhere. Then

$$\lim_{|\xi|\to\infty} \hat{I}(\xi) \neq 0,$$

which by Problem 1 shows that $I$ can not be in $L^1$, a contradiction.

### 3 Problem 3

### 3.1 (a)

### 3.1.1 (i)

Let $g(x) = f(x - y)$. We then have

$$\begin{aligned} \hat{g}(\xi) &:= \int g(x)e^{-2\pi i x \cdot \xi} \, dx \\ &= \int f(x - y)e^{-2\pi i x \cdot \xi} \, dx \\ &= \int f(x - y)e^{-2\pi i(x-y)\cdot\xi}e^{-2\pi i y \cdot \xi} \, dx \\ &= e^{-2\pi i y \cdot \xi} \int f(x - y)e^{-2\pi i(x-y)\cdot\xi} \, dx \\ &\quad (t = x - y, dt = dx) \\ &= e^{-2\pi i y \cdot \xi} \int f(t)e^{-2\pi i t \cdot \xi} \, dt \\ &= e^{-2\pi i y \cdot \xi} \hat{f}(\xi). \end{aligned}$$

### 3.1.2 (ii)

Let $h(x) = e^{2\pi i x \cdot y} f(x)$. We then have

$$\begin{aligned} \hat{h}(\xi) &:= \int e^{2\pi i x \cdot y} f(x)e^{-2\pi i x \cdot \xi} \, dx \\ &= \int e^{2\pi i x \cdot y - 2\pi i x \cdot \xi) f(x) \, dx \\ &= \int f(\xi - y)e^{-2\pi i x \cdot (\xi - y)} \, dx \\ &= \hat{f}(\xi - y). \end{aligned}$$

### 3.2 (b)

We'll use the fact that if $\langle \cdot, \cdot \rangle$ is an inner product on a vector space $V$ and $A$ is an invertible linear transformation, then for all $\mathbf{x}, \mathbf{y} \in V$ we have

$$\langle A\mathbf{x}, \mathbf{y} \rangle = \langle \mathbf{x}, A^T\mathbf{y} \rangle$$

<!-- page 64 -->

where $A^{-T}$ denotes the transpose of the inverse of $A$ (or $(A^{-1})^*$ if $V$ is complex).

We then have

$$\begin{array}{l} \frac{1}{|\det T|} \hat{f}(T^{-T} \xi) = \frac{1}{|\det T|} \int f(x) e^{-2\pi i x \cdot T^{-T} \xi} \, dx \\ \quad x \mapsto Tx, \, dx \mapsto |\det T| \, dx \\ = \frac{1}{|\det T|} \int f(Tx) e^{-2\pi i T x \cdot T^{-T} \xi} |\det T| \, dx \\ = \int f(Tx) e^{-2\pi i x \cdot \xi} \, dx \\ \quad \text{since } Tx \cdot T^{-T} \xi = T^{-1} Tx \cdot \xi = x \cdot \xi \\ = \widehat{(f \circ T)} (\xi). \end{array}$$

## 4 Problem 4

### 4.1 (a)

#### 4.1.1 (i)

Let $g(x) = xf(x)$. Then if an interchange of the derivative and the integral is justified, we have

$$\begin{array}{l} \frac{\partial}{\partial \xi} \hat{f}(\xi) := \frac{\partial}{\partial \xi} \int f(x) e^{-2\pi i x \cdot \xi} \, dx \\ \quad =? \int f(x) \frac{\partial}{\partial \xi} e^{-2\pi i x \cdot \xi} \, dx \\ \quad = \int f(x) 2\pi i x e^{-2\pi i x \cdot \xi} \, dx \\ \quad = 2\pi i \int x f(x) e^{-2\pi i x \cdot \xi} \, dx \\ \quad := 2\pi i \hat{g}(\xi). \end{array}$$

To see that the interchange is justified, we just note that we can apply the dominated convergence theorem, since $\int |f(x) e^{-2\pi i x \cdot \xi}| \leq \int |f| < \infty$, where we assumed $f \in L^1$.

#### 4.1.2 (ii)

We have

<!-- page 65 -->

$$\begin{array}{l} \hat{h}(\xi) := \int \frac{\partial f}{\partial x}(x) e^{-2\pi i x \cdot \xi} \, dx \\ = f(x) e^{-2\pi i x \cdot \xi} \Big|_{x=-\infty}^{x=\infty} - \int f(x)(2\pi i \xi) e^{-2\pi i x \cdot \xi} \, dx \\ \quad \text{(integrating by parts)} \\ = - \int f(x)(-2\pi i \xi) e^{-2\pi i x \cdot \xi} \, dx \\ \quad \text{(since } f(\infty) = f(-\infty) = 0) \\ = 2\pi i \xi \int f(x) e^{-2\pi i x \cdot \xi} \, dx \\ := 2\pi i \xi \hat{f}(\xi). \end{array}$$

### 4.2 (b)

Let $G(x) = e^{-\pi x^2}$ and $\partial_\xi$ be the operator that differentiates with respect to $\xi$.

Then

$$\partial_\xi \left( \frac{\hat{G}(\xi)}{G(\xi)} \right) = \frac{G(\xi) \partial_\xi \hat{G}(\xi) - \hat{G}(\xi) \partial_\xi G(\xi)}{G(\xi)^2},$$

and the claim is that this is zero. This happens precisely when the numerator is zero, so we'd like to show that

$$G(\xi) \partial_\xi \hat{G}(\xi) - \hat{G}(\xi) \partial_\xi G(\xi) = 0.$$

A direct computation shows that

$$\partial_\xi G(\xi) = -2\pi \xi G(\xi), \tag{1}$$

and we claim that $\partial_\xi \hat{G}(\xi) = -2\pi \xi \hat{G}(\xi)$ as well, which follows from the following computation:

<!-- page 66 -->

$$\begin{array}{l} \partial_{\xi}\hat{G}(\xi):=\partial_{\xi}\int G(x)e^{-2\pi ix\cdot\xi}\ dx \\ =\int G(x)\partial_{\xi}e^{-2\pi ix\cdot\xi}\ dx \\ =\int G(x)(-2\pi ix)e^{-2\pi ix\cdot\xi}\ dx \\ =\int G(x)(-2\pi ix)e^{-2\pi ix\cdot\xi}\ dx \\ =i\int 2\pi xG(x)e^{-2\pi ix\cdot\xi}\ dx \\ =i\int\partial_{x}G(x)e^{-2\pi ix\cdot\xi}\ dx\qquad\text{by (1)} \\ :=i\,\widehat{\partial_{x}G(x)}(\xi) \\ =i\,(2\pi i\xi\hat{G}(\xi))\qquad\text{by part (i)} \\ =-2\pi\xi\hat{G}(\xi). \end{array}$$

We can thus write

$$G(\xi)\partial_{\xi}\hat{G}(\xi)-\hat{G}(\xi)\partial_{\xi}G(\xi)=G(\xi)(-2\pi\xi\hat{G}(\xi))-\hat{G}(\xi)(-2\pi\xi G(\xi)),$$

which is patently zero.

It follows that $\frac{\hat{G}(\xi)}{G(\xi)}=c_{0}$ for some constant $c_{0}$, from which it follows that $\hat{G}(\xi)=c_{0}G(\xi)$.

Using the fact that $G(0)=1$ by direct evaluation and $\hat{G}(0)=\int G(x)\ dx=1$, we can conclude that $c_{0}=1$ and thus $\hat{G}(\xi)=G(\xi)$.

## 5 Problem 5

### 5.1 (a)

By a direct computation. we have

<!-- page 67 -->

$$\begin{array}{l} \hat{D}(\xi) := \int_{-\frac{1}{2}}^{\frac{1}{2}} 1 e^{-2\pi i x \xi} \, dx \\ = \int_{-\frac{1}{2}}^{\frac{1}{2}} \cos(-2\pi x \xi) + i \sin(-2\pi x \xi) \, dx \\ = \int_{-\frac{1}{2}}^{\frac{1}{2}} \cos(-2\pi x \xi) \, dx \\ \quad \text{(since sin is odd and the domain is symmetric about 0)} \\ = 2 \int_{0}^{\frac{1}{2}} \cos(-2\pi x \xi) \, dx \\ \quad \text{(since cos is even and the domain is symmetric about 0)} \\ = 2 \left( \frac{1}{2\pi\xi} \sin(-2\pi x \xi) \Big|_{x=0}^{x=\frac{1}{2}} \right) \\ = \frac{\sin(\pi\xi)}{\pi\xi}. \end{array}$$

### 5.2 (b)

#### 5.2.1 (i)

Since $F(x) = D(x) * D(x)$, we have $\hat{F}(\xi) = (\hat{D}(\xi))^2$ by question 2a, and so $\hat{F}(\xi) = \left( \frac{\sin(\pi\xi)}{\pi\xi} \right)^2$.

#### 5.2.2 (ii)

Letting $\mathcal{F}$ denote the Fourier transform operator, we have $\mathcal{F}^2(h)(\xi) = h(-\xi)$ for any $h \in L^1$. In particular, if $f$ is an even function, then $f(\xi) = -f(\xi)$ and $\mathcal{F}^2(f) = f$.

In this case, letting $F$ be the box function, $F$ can be seen to be even from its definition. Since $f := \mathcal{F}(F)$ by part (i), we have

$$\hat{f} := \mathcal{F}(f) = \mathcal{F}(\mathcal{F}(F)) = \mathcal{F}^2(F) = F,$$

which says that $\hat{f}(x) = F(x)$, the original box function.

### 5.3 (c)

By a direct computation of the integral in question, we have

<!-- page 68 -->

$$\begin{array}{l} I(x) := \int e^{-2\pi|\xi|} e^{2\pi i x \xi} \, d\xi \\ = \int_{-\infty}^{0} e^{-2\pi(-\xi)} e^{-2\pi i x \xi} \, d\xi + \int_{0}^{\infty} e^{2\pi\xi} e^{2\pi i x \xi} \, d\xi \\ = \int_{0}^{\infty} e^{-2\pi\xi} e^{-2\pi i x \xi} \, d\xi + \int_{0}^{\infty} e^{2\pi\xi} e^{2\pi i x \xi} \, d\xi \end{array}$$

by the change of variables $\xi \mapsto -\xi$, $d\xi \mapsto -d\xi$ and swapping integration bounds

$$= \int_{0}^{\infty} e^{-2\pi\xi} e^{-2\pi i x \xi} + e^{2\pi\xi} e^{2\pi i x \xi} \, d\xi$$

$$= \frac{1}{2\pi} \int_{0}^{\infty} e^{-u} e^{-ixu} + e^{-u} e^{ixu} \, du$$

$$= \frac{1}{2\pi} \int_{0}^{\infty} e^{-u(1+ix)} + e^{-u(1-ix)} \, du$$

$$= \frac{1}{2\pi} \left( \frac{-e^{-u(1+ix)}}{1+ix} \Big|_{u=0}^{u=\infty} + \frac{-e^{-u(1-ix)}}{1+ix} \Big|_{u=0}^{u=\infty} \right)$$

$$= \frac{1}{2\pi} \left( \frac{1}{1+ix} + \frac{1}{1-ix} \right)$$

$$= \frac{1}{2\pi} \frac{2}{1+x^2}$$

$$= \frac{1}{\pi} \frac{1}{1+x^2},$$

so $P(x) = I(x)$.

Then, by the Fourier inversion formula, we have

$$\begin{array}{l} I(x) = P(x) = \int \hat{P}(\xi) e^{-2\pi i x \xi} \, dx \\ \implies \int e^{-2\pi|\xi|} e^{2\pi i x \xi} = \int \hat{P}(\xi) e^{-2\pi i x \xi} \, dx \\ \implies \int e^{-2\pi|\xi|} e^{2\pi i x \xi} - \hat{P}(\xi) e^{-2\pi i x \xi} \, dx = 0 \\ \implies \int \left( e^{-2\pi|\xi|} - \hat{P}(\xi) \right) e^{-2\pi i x \xi} \, dx = 0 \\ \implies \left( e^{-2\pi|\xi|} - \hat{P}(\xi) \right) e^{-2\pi i x \xi} =_{a.e.} 0 \\ \implies e^{-2\pi|\xi|} =_{a.e.} \hat{P}(\xi), \end{array}$$

where equality is almost everywhere and follows from the fact that if $\int f = 0$ then $f = 0$ almost everywhere.

## 6 Problem 6

We first note that if $G_t(x) := t^{-n} e^{-\pi|x|^2/t^2}$, then $\hat{G}_t(\xi) = e^{-\pi t^2 |\xi|^2}$.

<!-- page 69 -->

Moreover, if an interchange of integrals is justified, we have have

$$\begin{array}{l} \|f\|_{1}:=\int_{\mathbb{R}^{n}}\left|\int_{0}^{\infty}G_{t}(x)e^{-\pi t^{2}}t^{2\varepsilon-1}\,dt\right|dx \\ =\int_{\mathbb{R}^{n}}\int_{0}^{\infty}G_{t}(x)e^{-\pi t^{2}}t^{2\varepsilon-1}\,dt\,dx \end{array}$$

since the integrand and thus integral is positive.

$$=?\int_{0}^{\infty}\int_{\mathbb{R}^{n}}G_{t}(x)e^{-\pi t^{2}}t^{2\varepsilon-1}\,dx\,dt$$

$$=\int_{0}^{\infty}e^{-\pi t^{2}}t^{2\varepsilon-1}\left(\int_{\mathbb{R}^{n}}G_{t}(x)\,dx\right)\,dt$$

$$=\int_{0}^{\infty}e^{-\pi t^{2}}t^{2\varepsilon-1}\,(1)\,dt$$

$$=\int_{0}^{\infty}e^{-\pi t^{2}}t^{2\varepsilon-1}\,dt,$$

which we claim is finite, so $f\in L^{1}$.

To see that the norm is finite, we note that

$$t\in[0,1]\implies e^{-\pi t^{2}}<1$$

and if we take $\varepsilon<\frac{1}{2}$, we have $2\varepsilon-1<0$ and thus

$$t\in[1,\infty)\implies t^{2\varepsilon-1}\leq 1.$$

Thus

$$\begin{array}{l} \int_{0}^{\infty}e^{-\pi t^{2}}t^{2\varepsilon-1}\,dt=\int_{0}^{1}e^{-\pi t^{2}}t^{2\varepsilon-1}\,dt+\int_{1}^{\infty}e^{-\pi t^{2}}t^{2\varepsilon-1}\,dt \\ \leq\int_{0}^{1}t^{2\varepsilon-1}\,dt+\int_{1}^{\infty}e^{-\pi t^{2}}\,dt \\ \leq\int_{0}^{1}t^{2\varepsilon-1}\,dt+\int_{0}^{\infty}e^{-\pi t^{2}}\,dt \\ =\frac{1}{2\varepsilon}+\frac{1}{2}<\infty, \end{array}$$

where the first term is obtained by directly evaluating the integral, and the second is derived from the fact that its integral over the real line is 1 and it is an even function.

Justifying the interchange: we note that the integrand $G_{t}(x)e^{-\pi t^{2}}t^{2\varepsilon-1}$ is non-negative, and we've just showed that one of the iterated integrals is absolutely convergent, so Tonelli will apply if the integrand is measurable. But $G_{t}(x)$ is a continuous function on $\mathbb{R}^{n}$ and the remaining terms are continuous on $\mathbb{R}$, so they are all measurable on $\mathbb{R}^{n}$ and $\mathbb{R}$ respectively. But then taking cylinders on everything in sight yields measurable functions, and the product of measurable functions is measurable.

If another interchange of integrals is justified, we can compute

<!-- page 70 -->

$$\hat{f}(\xi) := \int_{\mathbb{R}^n} \left( \int_0^\infty G_t(x) e^{-\pi t^2} t^{2\varepsilon - 1} \, dt \right) e^{-2\pi i x \cdot \xi} \, dx$$

$$= \int_{\mathbb{R}^n} \int_0^\infty G_t(x) e^{-\pi t^2} t^{2\varepsilon - 1} e^{-2\pi i x \cdot \xi} \, dt \, dx$$

$$=? \int_0^\infty \int_{\mathbb{R}^n} G_t(x) e^{-\pi t^2} t^{2\varepsilon - 1} e^{-2\pi i x \cdot \xi} \, dx \, dt$$

$$= \int_0^\infty e^{-\pi t^2} t^{2\varepsilon - 1} \left( \int_{\mathbb{R}^n} G_t(x) e^{-2\pi i x \cdot \xi} \, dx \right) \, dt$$

$$= \int_0^\infty e^{-\pi t^2} t^{2\varepsilon - 1} \hat{G}_t(\xi) \, dt$$

$$= \int_0^\infty e^{-\pi t^2} t^{2\varepsilon - 1} e^{-\pi t^2 |\xi|^2} \, dt$$

$$= \int_0^\infty e^{-\pi t^2 (1 + |\xi|^2)} t^{2\varepsilon - 1} \, dt$$

$$= \int_0^\infty e^{-\pi (t \sqrt{1 + |\xi|^2})^2} t^{2\varepsilon - 1} \, dt$$

$$s = t \sqrt{1 + |\xi|^2}, \, ds = \sqrt{1 + |\xi|^2} \, dt$$

$$= \int_0^\infty e^{-\pi s^2} \left( \frac{s}{\sqrt{1 - |\xi|^2}} \right)^{2\varepsilon - 1} \frac{1}{\sqrt{1 + |\xi|^2}} \, ds$$

$$= (1 + |\xi|^2)^{-\frac{2\varepsilon - 1}{2}} (1 + |\xi|^2)^{-\frac{1}{2}} \int_0^\infty e^{-\pi s^2} s^{2\varepsilon - 1} \, ds$$

$$= (1 + |\xi|^2)^{-\varepsilon} \int e^{-\pi t^2} t^{2\varepsilon - 1} \, dt$$

$$:= F(\xi) \|f\|_1.$$

To see that the interchange is justified, note that

$$\int_{\mathbb{R}^n} \int_0^\infty \left| G_t(x) e^{-\pi t^2} t^{2\varepsilon - 1} e^{-2\pi i x \cdot \xi} \right| \, dt \, dx = \int_{\mathbb{R}^n} \int_0^\infty \left| G_t(x) e^{-\pi t^2} t^{2\varepsilon - 1} \right| \, dt \, dx,$$

since $|e^{2\pi i x \cdot \xi}| = 1$. The integrand appearing is precisely what we showed was measurable when computed $\|f\|_1$ above, so Tonelli applies.

Thus $F(\xi)$ is the Fourier transform of the function $g(x) := f(x)/\|f\|_1$. $\square$

<!-- page 71 -->

# Problem Set 7

D. Zack Garza

November 14, 2019

## Contents

|  **1** | **Problem 1** | **1**  |
| --- | --- | --- |
|  1.1 | Part a | 1  |
|  1.2 | Part b | 2  |
|  **2** | **Problem 2** | **3**  |
|  2.1 | Part a: | 4  |
|  2.2 | Part b: | 4  |
|  **3** | **Problem 3** | **5**  |
|  3.1 | Part a | 5  |
|  3.2 | Part b | 5  |
|  **4** | **Problem 4** | **6**  |
|  4.1 | Part a | 6  |
|  4.1.1 | i | 6  |
|  4.1.2 | ii | 7  |
|  4.2 | Part b | 7  |
|  4.2.1 | i | 7  |
|  4.2.2 | ii | 8  |
|  **5** | **Problem 5** | **9**  |
|  5.1 | Part 1 | 9  |
|  5.2 | Part b | 10  |
|  5.3 | Part c | 10  |
|  **6** | **Problem 6** | **11**  |
|  6.1 | Part a | 11  |
|  6.2 | Part b | 11  |

## 1 Problem 1

### 1.1 Part a

We want to show that $\ell^2(\mathbb{N})$ is complete, so let $\{x_n\} \subseteq \ell^2(\mathbb{N})$ be a Cauchy sequence. We then have $\|x^j - x^k\|_{\ell^2} \to 0$, and we want to produce some $\mathbf{x} := \lim_{n \rightarrow \infty} x^n$ such that $x \in \ell^2$.

1

<!-- page 72 -->

To this end, for each fixed index $i$, define

$$\mathbf{x}_i := \lim_{n \to \infty} x_i^n.$$

This is well-defined since $\|x^j - x^k\|_{\ell^2} = \sum_i |x_i^j - x_i^k|^2 \to 0$, and since this is a sum of positive real numbers that approaches zero, each term must approach zero. But then for a fixed $i$, the sequence $|x_i^j - x_i^k|^2$ is a Cauchy sequence of real numbers which necessarily converges by the completeness of $\mathbb{R}$.

We also have $\|\mathbf{x} - x^j\|_{\ell^2} \to 0$ since

$$\|\mathbf{x} - x^j\|_{\ell^2} = \|\lim_{k \to \infty} x^k - x^j\|_{\ell^2} = \lim_{k \to \infty} \|x^k - x^j\|_{\ell^2} \to 0$$

where the limit can be passed through the norm because the map $t \mapsto \|t\|_{\ell^2}$ is continuous. So $x^j \to \mathbf{x}$ in $\ell^2$ as well.

It remains to show that $\mathbf{x} \in \ell^2(\mathbb{N})$, i.e. that $\sum_i |\mathbf{x}_i|^2 < \infty$. To this end, we write

$$\begin{aligned} \|\mathbf{x}\|_{\ell^2} &= \|\mathbf{x} - x^j + x^j\|_{\ell^2} \\ &\leq \|\mathbf{x} - x^j\|_{\ell^2} + \|x^j\|_{\ell^2} \\ &\to M < \infty, \end{aligned}$$

where $\lim_j \|\mathbf{x} - x^j\|_{\ell^2} = 0$ by the previous argument, and the second term is bounded because $x^j \in \ell^2 \iff \|x^j\|_{\ell^2} := M < \infty$. $\square$

### 1.2 Part b

Let $H$ be a Hilbert space with inner product $\langle \cdot, \cdot \rangle$ and induced norm $\|\cdot\|$.

Lemma: For any complex number $z$, we have

$$\Im(z) = \Re(-iz),$$

and as a corollary, since the inner product on $H$ takes values in $\mathbb{C}$, we have

$$\Re(\langle x, \ i y \rangle) = \Re(-i\langle x, \ y \rangle) = \Im(\langle x, \ y \rangle).$$

2

<!-- page 73 -->

We can compute the following:

$$\|x + y\|^2 = \|x\|^2 + \|y\|^2 + 2 \Re(\langle x, y \rangle)$$

$$\|x - y\|^2 = \|x\|^2 + \|y\|^2 - 2 \Re(\langle x, y \rangle)$$

$$\|x + iy\|^2 = \|x\|^2 + \|y\|^2 + 2 \Re(\langle x, iy \rangle)$$

$$= \|x\|^2 + \|y\|^2 + \Im(\langle x, y \rangle)$$

$$\|x - iy\|^2 = \|x\|^2 + \|y\|^2 - 2 \Re(\langle x, iy \rangle)$$

$$= \|x\|^2 + \|y\|^2 + \Im(\langle x, y \rangle)$$

and summing these all

$$\begin{array}{l} \|x + y\|^2 - \|x - y\|^2 + i\|x + iy\|^2 - i\|x + iy\| = 4 \Re(\langle x, y \rangle) + 4i \Im(\langle x, y \rangle) \\ = 4\langle x, y \rangle. \end{array}$$

To conclude that a linear map $U$ is an isometry iff $U$ is unitary, if we assume $U$ is unitary then we can write

$$\|x\|^2 := \langle x, x \rangle = \langle Ux, Ux \rangle := \|Ux\|^2.$$

Assuming now that $U$ is an isometry, by the polarization identity we can write

$$\begin{array}{l} \langle Ux, Uy \rangle = \frac{1}{4} \left( \|Ux + Uy\|^2 + \|Ux - Uy\|^2 + i\|Ux + Uy\|^2 - i\|Ux + Uy\|^2 \right) \\ = \frac{1}{4} \left( \|U(x + y)\|^2 + \|U(x - y)\|^2 + i\|U(x + y)\|^2 - i\|U(x + y)\|^2 \right) \\ = \frac{1}{4} \left( \|x + y\|^2 + \|x - y\|^2 + i\|x + y\|^2 - i\|x + y\|^2 \right) \\ = \langle x, y \rangle. \end{array}$$

## 2 Problem 2

Lemma: The map $\langle \cdot, \cdot \rangle : H \times H \to \mathbb{R}$ is continuous.

Proof:

Let $x_n \to x$ and $y_n \to y$, then

3

<!-- page 74 -->

$$\begin{aligned} |\langle x_n, y_n \rangle - \langle x, y \rangle| &= |\langle x_n, y_n \rangle - \langle x, y_n \rangle + \langle x, y_n \rangle - \langle x, y \rangle| \\ &= |\langle x_n - x, y_n \rangle + \langle x, y_n - y \rangle| \\ &\leq \|x_n - x\| \|y_n\| + \|x\| \|y_n - y\| \\ &\to 0 \cdot M + C \cdot 0 < \infty, \end{aligned}$$

where $\|y_n\| \to \|y\| := M < \infty$ since $y \in H$ implies that $\|y\|$ is finite.

## 2.1 Part a:

We want to show that sequences in $E^\perp$ converge to elements of $E^\perp$. Using the lemma, letting $\{e_n\}$ be a sequence in $E^\perp$, so $y \in E \implies \langle e_n, y \rangle = 0$. Since $H$ is complete, $e_n \to e \in H$; we can show that $e \in E^\perp$ by letting $y \in E$ be arbitrary and computing

$$\langle e, y \rangle = \left\langle \lim_n e_n, y \right\rangle = \lim_n \langle e_n, y \rangle = \lim_n 0 = 0,$$

so $e \in E^\perp$.

## 2.2 Part b:

Let $S := \text{span}_H(E)$; then the smallest closed subspace containing $E$ is $\overline{S}$, the closure of $S$. We will proceed by showing that $E^{\perp\perp} = \overline{S}$.

$$\overline{S} \subseteq E^{\perp\perp}:$$

Let $\{x_n\}$ be a sequence in $S$, so $x_n \to x \in \overline{S}$.

First, each $x_n$ is in $E^{\perp\perp}$, since if we write $x_n = \sum a_i e_i$ where $e_i \in E$, we have

$$y \in E^\perp \implies \langle x_n, y \rangle = \left\langle \sum_i a_i e_i, y \right\rangle = \sum_i a_i \langle e_i, y \rangle = 0 \implies x_n \in (E^\perp)^\perp.$$

It remains to show that $x \in E^{\perp\perp}$, which follows from

$$y \in E^\perp \implies \langle x, y \rangle = \left\langle \lim_n x_n, y \right\rangle = \lim_n \langle x_n, y \rangle = 0 \implies x \in (E^\perp)^\perp,$$

where we've used continuity of the inner product.

$$E^{\perp\perp} \subseteq \overline{S}:$$

For notational convenience, let $S_c$ denote the closure $\overline{S}$. Let $x \in E^{\perp\perp}$. Noting that $S_c$ is closed, we can define $P$, the operator projecting elements onto $S_c$, and write

$$x = Px + (x - Px) \in S_c \oplus S_c^\perp$$

4

<!-- page 75 -->

But since $\langle x, x - Px \rangle = 0$ (because $x - Px \in E^{\perp}$ and $x \in (E^{\perp})^{\perp}$), we can rewrite the first term in this inner product to obtain

$$0 = \langle x, x - Px \rangle = \langle Px + (x - Px), x - Px \rangle = \langle Px, x - Px \rangle + \langle x - Px, x - Px \rangle,$$

where we can note that the first term is zero because $Px \in S_c$ and $x - Px \in S_c^{\perp}$, and the second term is $\|x - Px\|^2$.

But this says $\|x - Px\|^2 = 0$, so $x - Px = 0$ and thus $x = Px \in S_c$, which is what we wanted to show.

### 3 Problem 3

#### 3.1 Part a

We compute

$$\|e_0\|^2 = \int_0^1 1^2 \, dx = 1$$

$$\|e_1\|^2 = \int_0^1 3(2x - 1)^2 = \frac{1}{2}(2x - 1)^2 \Big|_0^1 = 1$$

$$\langle e_0, e_1 \rangle = \int_0^1 \sqrt{3}(2x - 1) \, dx = \frac{\sqrt{3}}{4}(2x - 1) \Big|_0^1 = 0.$$

which verifies that this is an orthonormal system.

#### 3.2 Part b

We first note that this system spans the degree 1 polynomials in $L^2([0, 1])$, since we have

$$\left[ \begin{array}{cc} 1 & 0 \\ 2\sqrt{3} & \sqrt{3} \end{array} \right] [1, x]^t = [e_0, e_1]$$

which exhibits a matrix that changes basis from $\{1, x\}$ to $\{e_0, e_1\}$ which is invertible, so both sets span the same subspace.

Thus the closest degree 1 polynomial $f$ to $x^3$ is given by the projection onto this subspace, and since $\{e_i\}$ is orthonormal this is given by

5

<!-- page 76 -->

$$\begin{array}{l} f(x) = \sum_{i} \left\langle x^{3}, e_{i} \right\rangle e_{i} \\ = \left\langle x^{3}, 1 \right\rangle 1 + \left\langle x^{3}, \sqrt{3}(2x - 1) \right\rangle \sqrt{3}(2x - 1) \\ = \int_{0}^{1} x^{2} \, dx + \sqrt{3}(2x - 1) \int_{0}^{1} \sqrt{3}x^{2}(2x - 1) \, dx \\ = \frac{1}{3} + \sqrt{3}(2x - 1) \frac{\sqrt{3}}{6} \\ = x - \frac{1}{6}. \end{array}$$

We can also compute

$$\begin{array}{l} \|f - g\|_{2}^{2} = \int_{0}^{1} (x^{2} - x + \frac{1}{6})^{2} \, dx \\ = \frac{1}{180} \\ \implies \|f - g\|_{2} = \frac{1}{\sqrt{180}}. \end{array}$$

## 4 Problem 4

### 4.1 Part a

#### 4.1.1 i

We can first note that $\left\langle 1/\sqrt{2}, \cos(2\pi nx) \right\rangle = \left\langle 1/\sqrt{2}, \sin(2\pi mx) \right\rangle = 0$ for any $n$ or $m$, since this involves integrating either sine or cosine over an integer multiple of its period.

Letting $m, n \in \mathbb{Z}$, we can then compute

$$\begin{array}{l} \langle \cos(2\pi nx), \sin(2\pi mx) \rangle = \int_{0}^{1} \cos(2\pi nx) \sin(2\pi mx) \, dx \\ = \frac{1}{2} \int_{0}^{1} \sin(2\pi(n + m)x) - \sin(2\pi(n - m)x) \, dx \\ = \frac{1}{2} \int_{0}^{1} \sin(2\pi(n + m)x) - \frac{1}{2} \int_{0}^{1} \sin(2\pi(n - m)x) \, dx \\ = 0, \end{array}$$

which again follows from integration of sine over a multiple of its period (where we use the fact that $m + n, m - n \in \mathbb{Z}$).

Similarly,

6

<!-- page 77 -->

$$\begin{array}{l} \langle \cos (2 \pi n x), \cos (2 \pi m x) \rangle = \int_ {0} ^ {1} \cos (2 \pi n x) \cos (2 \pi m x) d x \\ = \frac {1}{2} \int_ {0} ^ {1} \cos (2 \pi (m + n) x) + \cos (2 \pi (m - n) x) d x \\ = \left\{ \begin{array}{l l} \frac {1}{2} \int_ {0} ^ {1} \cos (4 \pi n x) + 1 d x = 1 & m = n \\ 0 & m \neq n \end{array} \right.. \\ \end{array}$$

$$\begin{array}{l} \langle \sin (2 \pi n x), \sin (2 \pi m x) \rangle = \int_ {0} ^ {1} \sin (2 \pi n x) \sin (2 \pi m x) d x \\ = \frac {1}{2} \int_ {0} ^ {1} \cos (2 \pi (m - n) x) + \cos (2 \pi (m + n) x) d x \\ = \left\{ \begin{array}{l l} \frac {1}{2} \int_ {0} ^ {1} 1 + \cos (4 \pi n x) d x = 1 & m = n \\ 0 & m \neq n \end{array} \right.. \\ \end{array}$$

Thus each pairwise combination of elements are orthonormal, making the entire set orthonormal.

### 4.1.2 ii

We have

$$\begin{array}{l} \left\langle e ^ {2 \pi k x}, e ^ {- 2 \pi i \ell x} \right\rangle = \int_ {0} ^ {1} e ^ {2 \pi i k x} \overline {{e ^ {2 \pi i \ell x}}} d x \\ = \int_ {0} ^ {1} e ^ {2 \pi i k x} e ^ {- 2 \pi i \ell x} d x \\ = \int_ {0} ^ {1} e ^ {2 \pi i (k - \ell) x} d x \\ (= \int_ {0} ^ {1} 1 d x = 1 \quad \text { if } k = \ell , \text { otherwise: }) \\ = \left. \frac {e ^ {2 \pi i (k - \ell) x}}{2 \pi i (k - \ell)} \right| _ {0} ^ {1} \\ = \frac {e ^ {2 \pi i (k - \ell)} - 1}{2 \pi i (k - \ell)} \\ = 0, \\ \end{array}$$

since $e^{2\pi ik} = 1$ for every $k \in Z$, and $k - \ell \in \mathbb{Z}$. Thus this set is orthonormal.

## 4.2 Part b

### 4.2.1 i

By the Weierstrass approximation theorem for functions on a bounded interval, we can find a polynomials $P_{n}(x)$ such that $\| f - P_{n}\|_{\infty}\to 0$, i.e. the $P_{n}$ uniformly approximate $f$ on $[0,1]$.

7

<!-- page 78 -->

Letting $\varepsilon > 0$, we can thus choose a $P$ such that $\|f - P\|_{\infty} < \varepsilon$, which necessarily implies that $\|f - P\|_{L^1} < \varepsilon$ since we have

$$\int_0^1 |f(x) - P(x)| \, dx \leq \int_0^1 \varepsilon \, dx = \varepsilon.$$

Thus we can write

$$f(x) = P(x) + (f(x) - P(x))$$

where $h(x) := f(x) - P(x)$ satisfies $\|h\|_{L^1} < \varepsilon$. It only remains to show that $P \in L^2([0, 1])$, but this follows from the fact that any polynomial on a compact interval is uniformly bounded, say $|P(x)| \leq M < \infty$ for all $x \in [0, 1]$, and thus

$$\|P\|_{L^2}^2 = \int_0^1 |P(x)|^2 \, dx \leq \int_0^1 M^2 \, dx = M^2 < \infty.$$

It follows that we can let $g = P$ and $h = f - P$ to obtain the desired result.

### 4.2.2 ii

By part (i), the claim is that it suffices to show this is true for $f \in L^2$. In this case, we can identify

$$\int_0^1 f(x) \cos(2\pi kx) \, dx := \Re(\hat{f}(k))$$

$$\int_0^1 f(x) \sin(2\pi kx) \, dx := \Im(\hat{f}(k)),$$

the real and imaginary parts of the $k$th Fourier coefficient of $f$ respectively.

By Bessel's inequality, we know that $\left\{\hat{f}(k)\right\}_{k \in \mathbb{N}} \in \ell^1(\mathbb{N})$, and so $\sum_k |\hat{f}(k)| < \infty$.

But this is a convergent sequence of real numbers, which necessarily implies that $|\hat{f}(k)| \to 0$. In particular, this also means that its real and imaginary parts tend to zero, which is exactly what we wanted to show.

If we instead have $f \in L^1$, write $f = g + h$ where $g \in L^2$ and $\|h\|_{L^1} \to 0$. Then

$$\begin{aligned} \left| \int_0^1 f(x) \cos(2\pi kx) \, dx \right| &= \left| \int_0^1 (g(x) + h(x)) \cos(2\pi kx) \, dx \right| \\ &\leq \left| \int_0^1 g(x) \cos(2\pi kx) \, dx \right| + \left| \int_0^1 h(x) \cos(2\pi kx) \, dx \right| \\ &\leq \left| \int_0^1 g(x) \cos(2\pi kx) \, dx \right| + \int_0^1 |h(x)| |\cos(2\pi kx)| \, dx \\ &= |\hat{g}(k)| + \varepsilon \\ &\to 0, \end{aligned}$$

with a similar computation for $\int f(x) \sin(2\pi kx)$. $\square$

8

<!-- page 79 -->

# 5 Problem 5

## 5.1 Part 1

We use the following algorithm: given $\{v\}_i$, we set

- \(e_1 = v_1\), and then normalize to obtain \(\hat{e}_1 = e_1 / \| e_1\|\)
- \(e_i = v_i - \sum_{k\leq i - 1}\langle v_i,\hat{e}_i\rangle \hat{e}_i\)

The result set $\{\hat{e}_i\}$ is the orthonormalized basis.

We set $e_1 = 1$, and check that $\|e_1\|^2 = 2$, and thus set $\hat{e}_1 = \frac{1}{\sqrt{2}}$.

We then set

$$\begin{array}{l} e_2 = x - \langle x, \hat{e}_1 \rangle \hat{e}_1 \\ = x - \langle x, 1 \rangle 1 \\ = x - \int_{-1}^{1} \frac{1}{\sqrt{2}} x \, dx \\ = x - \int \text{odd function} \\ = x, \end{array}$$

and so $e_2 = x$. We can then check that

$$\|e_2\| = \left( \int_{-1}^{1} x^2 \, dx \right)^{1/2} = \sqrt{\frac{2}{3}},$$

and so we set $\hat{e}_2 = \sqrt{\frac{3}{2}} x$.

We continue to compute

$$\begin{array}{l} e_3 = x^2 - \langle x^2, \hat{e}_1 \rangle \hat{e}_1 - \langle x^2, \hat{e}_2 \rangle \hat{e}_2 \\ = x^2 - \frac{1}{2} \int_{-1}^{1} x^2 \, dx - \frac{3}{2} x \int_{-1}^{1} x^3 \, dx \\ = x^2 - \left( \frac{1}{6} x^3 \right) \big|_{-1}^{1} + \frac{3}{2} x \int_{-1}^{1} \text{odd function} \\ = x^2 - \frac{1}{3}. \end{array}$$

We can then check that $\|e_3\|^2 = \frac{8}{45}$, so we set

9

<!-- page 80 -->

$$\begin{aligned} \hat{e}_3 &= \sqrt{\frac{45}{8}}(x^2 - \frac{1}{3}) \\ &= \frac{1}{2}\sqrt{\frac{45}{2}}\frac{1}{3}(3x^2 - 1) \\ &= \frac{1}{3}\sqrt{\frac{45}{2}}\left(\frac{3x^2 - 1}{2}\right). \end{aligned}$$

In summary, this yields

$$\begin{aligned} \hat{e}_1 &= \frac{1}{\sqrt{2}} \\ \hat{e}_2 &= x \\ \hat{e}_3 &= \frac{1}{3}\sqrt{\frac{45}{2}}\left(\frac{3x^2 - 1}{2}\right), \end{aligned}$$

which are scalar multiples of the first three Legendre polynomials.

## 5.2 Part b

Let $p(x) = a + bx + cx^2$, we are then looking for $p$ such that $\|x^3 - p(x)\|_2^2$ is minimized. Noting that

$$p(x) \in \operatorname{span}\left\{1, x, x^2\right\} = \operatorname{span}\left\{P_0(x), P_1(x), P_2(x)\right\} := S,$$

we can conclude that $p(x)$ will be the projection of $x^3$ onto $S$. Thus $p(x) = \sum_{i=0}^2 \langle x^3, \hat{e}_i \rangle \hat{e}_i$.

Proceeding to compute the terms in this expansion, we can note that $\langle x^3, f \rangle$ for any $f$ that is even will result in integrating an odd function over a symmetric interval, yielding zero. So only one term doesn't vanish:

$$\langle x^3, x \rangle x = x \int_{-1}^1 x^4 \, dx = \frac{2}{5}x$$

And thus $p(x) = \frac{2}{5}x$ is the minimizer.

## 5.3 Part c

The first three conditions necessitate $g \in S^\perp$ and $\|g\| = 1$. Since $S$ is a closed subspace, we can write $x^3 = p(x) + (x^3 - p(x)) \in S \oplus S^\perp$, and so $x^3 - p(x) \in S^\perp$.

The claim is that $g(x) := x^3 - p(x)$ is a scalar multiple of the desired maximizer. This follows from the fact that

$$\left| \langle x^3 - p, g \rangle \right| \leq \|x^3 - p\| \|g\|$$

10

<!-- page 81 -->

by Cauchy-Schwarz, with equality precisely when $g = \lambda(x^3 - p)$ for some scalar $\lambda$. However, the restriction $\|g\| = 1$ forces $\lambda = \|x^3 - p\|^{-1}$.

A computation shows that

$$\|x^3 - p\|^2 = \int_0^1 (x^3 - \frac{2}{5}x)^2 \, dx = \frac{19}{525},$$

and so we can take

$$g(x) := \frac{25}{\sqrt{19}} \left( x^3 - \frac{2}{5}x \right).$$

## 6 Problem 6

### 6.1 Part a

To see that $g \in \mathcal{C}$, we can compute

$$\langle g, 1 \rangle = \int_0^1 18x^2 - 5 \, dx = 6 - 5 = 1$$

$$\langle g, x \rangle = \int_0^1 18x^3 - 5x \, dx = \frac{18}{4} - \frac{5}{2} = 2.$$

To see that $\mathcal{C} = g + S^\perp$, let $f \in \mathcal{C}$, so $\langle f, 1 \rangle = 1$ and $\langle f, x \rangle = 2$. We can then conclude that $f - g \in S^\perp$, since we have

$$\langle f - g, 1 \rangle = \langle f, 1 \rangle - \langle g, 1 \rangle = 1 - 1 = 0$$

$$\langle f - g, x \rangle = \langle f, x \rangle - \langle g, x \rangle = 2 - 2 = 0.$$

### 6.2 Part b

Note that this equivalent to finding an $f_0 \in \mathcal{C}$ such that $\|f_0\|$ is minimized.

Letting $f_0 \in \mathcal{C}$, be arbitrary and noting that by part (a) we have $f_0 = g + s$ where $s \in S^\perp$, we can compute

$$\begin{aligned} \|f_0\|^2 &= \langle f_0, f_0 \rangle \\ &= \langle g + s, g + s \rangle \\ &= \|g\|^2 + 2\Re\langle g, s \rangle + \|s\|^2, \end{aligned}$$

which can be minimized by taking $s = 0$, which forces $\|s\|^2 = 0$ and $\langle g, s \rangle = 0$. But this imposes the condition $f_0 = g + 0 = g$. $\square$

11

<!-- page 82 -->

# Problem Set 8

D. Zack Garza

November 28, 2019

## Contents

|  **1** | **Problem 1** | **1**  |
| --- | --- | --- |
|  1.1 | Part a | 1  |
|  1.2 | Part b | 2  |
|  1.3 | Part c | 2  |
|  **2** | **Problem 2** | **3**  |
|  2.1 | Part a | 3  |
|  2.1.1 | Part i | 3  |
|  2.1.2 | Part ii | 4  |
|  2.2 | Part b | 5  |
|  **3** | **Problem 3** | **5**  |
|  **4** | **Problem 4** | **7**  |
|  4.1 | Part a | 7  |
|  4.2 | Part b | 7  |
|  **5** | **Problem 5** | **8**  |
|  5.1 | Part a | 8  |
|  5.2 | Part b | 9  |
|  **6** | **Problem 6** | **10**  |

## 1 Problem 1

### 1.1 Part a

It follows from the definition that  $\|f\|_\infty = 0 \iff f = 0$  almost everywhere, and if  $\|f\|_\infty$  is the best upper bound for  $f$  almost everywhere, then  $\|cf\|_\infty$  is the best upper bound for  $cf$  almost everywhere.

So it remains to show the triangle inequality. Suppose that  $|f(x)| \leq \|f\|_\infty$  a.e. and  $|g(x)| \leq \|g\|_\infty$  a.e., then by the triangle inequality for the  $|\cdot|_\mathbb{R}$  we have

1

<!-- page 83 -->

$$\begin{array}{rl} |(f+g)(x)| \leq |f(x)| + |g(x)| & a.e. \\ \leq \|f\|_{\infty} + \|g\|_{\infty} & a.e., \end{array}$$

which means that $\|f+g\|_{\infty} \leq \|f\|_{\infty} + \|g\|_{\infty}$ as desired.

### 1.2 Part b

$\implies$ : Suppose $\|f_n - f\|_{\infty} \to 0$, then for every $\varepsilon$, $N_{\varepsilon}$ can be chosen large enough such that $|f_n(x) - f(x)| < \varepsilon$ a.e., which precisely means that there exist sets $E_{\varepsilon}$ such that $x \in E_{\varepsilon} \implies |f_n(x) - f(x)|$ and $m(E_{\varepsilon}^c) = 0$.

But then taking the sequence $\varepsilon_n := \frac{1}{n} \to 0$, we have $f_n \rightrightarrows f$ uniformly on $E := \bigcap_n E_n$ by definition, and $E^c = \bigcup_n E_n^c$ is still a null set.

$\iff$ : Suppose $f_n \rightrightarrows f$ uniformly on some set $E$ and $m(E^c) = 0$. Then for any $\varepsilon$, we can choose $N$ large enough such that $|f_n(x) - f(x)| < \varepsilon$ on $E$; but then $\varepsilon$ is an upper bound for $f_n - f$ almost everywhere, so $\|f_n - f\|_{\infty} < \varepsilon \to 0$.

### 1.3 Part c

To see that simple functions are dense in $L^{\infty}(X)$, we can use the fact that $f \in L^{\infty}(X) \iff$ there exists a $g$ such that $f = g$ a.e. and $g$ is bounded.

Then there is a sequence $s_n$ of simple functions such that $\|s_n - g\|_{\infty} \to 0$, which follows from a proof in Folland:

$$\text{Proof.} \quad (\text{a}) \text{ For } n = 0, 1, 2, \dots \text{ and } 0 \leq k \leq 2^{2n} - 1, \text{ let}$$

$$E_n^k = f^{-1}((k2^{-n}, (k+1)2^{-n}]) \quad \text{and} \quad F_n = f^{-1}((2^n, \infty]),$$

and define

$$\phi_n = \sum_{k=0}^{2^{2n}-1} k2^{-n}\chi_{E_n^k} + 2^n\chi_{F_n}.$$

(This formula is messy in print but easily understood graphically; see Figure 2.1.) It is easily checked that $\phi_n \leq \phi_{n+1}$ for all $n$, and $0 \leq f - \phi_n \leq 2^{-n}$ on the set where $f \leq 2^n$. The result therefore follows.

2

<!-- page 84 -->

![img-4.jpeg](img-4.jpeg)

![img-5.jpeg](img-5.jpeg)

However, $C_c^0(X)$ is dense $L^\infty(X) \iff$ every $f \in L^\infty(X)$ can be approximated by a sequence $\{g_k\} \subset C_c^0(X)$ in the sense that $\|f - g_n\|_\infty \to 0$. To see why this can not be the case, let $f(x) = 1$, so $\|f\|_\infty = 1$ and let $g_n \to f$ be an arbitrary sequence of $C_c^0$ functions converging to $f$ pointwise.

Since every $g_n$ has compact support, say $\text{supp}(g_n) := E_n$, then $g_n|_{E_n^c} \equiv 0$ and $m(E_n^c) > 0$. In particular, this means that $\|f - g_n\|_\infty = 1$ for every $n$, so $g_n$ can not converge to $f$ in the infinity norm.

## 2 Problem 2

### 2.1 Part a

#### 2.1.1 Part i

Lemma: $\|1\|_p = m(X)^{1/p}$

This follows from $\|1\|_p^p = \int_X |1|^p = \int_X 1 = m(X)$ and taking $p$th roots. $\square$

By Holder with $p = q = 2$, we can now write

$$\|f\|_1 = \|1 \cdot f\|_1 \le \|1\|_2 \|f\|_2 = m(X)^{1/2} \|f\|_2$$

$$\implies \|f\|_1 \le m(X)^{1/2} \|f\|_2.$$

Letting $M := \|f\|_\infty$, We also have

$$\|f\|_2^2 = \int_X |f|^2 \le \int_X |M|^2 = M^2 \int_X 1 = M^2 m(X)$$

$$\implies \|f\|_2 \le m(X)^{1/2} \|f\|_\infty$$

$$\implies m(X)^{1/2} \|f\|_2 \le m(X) \|f\|_\infty,$$

and combining these yields

$$\|f\|_1 \le m(X)^{1/2} \|f\|_2 \le m(X) \|f\|_\infty,$$

3

<!-- page 85 -->

from which it immediately follows

$$m(X) < \infty \implies L^\infty(X) \subseteq L^2(X) \subseteq L^1(X).$$

# **The Inclusions Are Strict:**

1. $\exists f \in L^1(X) \setminus L^2(X)$:

Let $X = [0, 1]$ and consider $f(x) = x^{-\frac{1}{2}}$. Then

$$\|f\|_1 = \int_0^1 x^{-\frac{1}{2}} < \infty \quad \text{by the } p \text{ test,}$$

while

$$\|f\|_2^2 = \int_0^1 x^{-1} \to \infty \quad \text{by the } p \text{ test.}$$

2. $\exists f \in L^2(X) \setminus L^\infty(X)$:

Take $X = [0, 1]$ and $f(x) = x^{-\frac{1}{4}}$. Then

$$\|f\|_2^2 = \int_0^1 x^{-\frac{1}{4}} < \infty \quad \text{by the } p \text{ test,}$$

while $\|f\|_\infty > M$ for any finite $M$, since $f$ is unbounded in neighborhoods of 0, so $\|f\|_\infty = \infty$.

# **2.1.2 Part ii**

1. $\exists f \in L^2(X) \setminus L^1(X)$ when $m(X) = \infty$:

Take $X = [1, \infty)$ and let $f(x) = x^{-1}$, then

$$\|f\|_2^2 = \int_0^\infty x^{-2} < \infty \quad \text{by the } p \text{ test,}$$

$$\|f\|_1 = \int_0^\infty x^{-1} \to \infty \quad \text{by the } p \text{ test.}$$

2. $\exists f \in L^\infty(X) \setminus L^2(X)$ when $m(X) = \infty$:

Take $X = \mathbb{R}$ and $f(x) = 1$. then

$$\|f\|_\infty = 1$$

$$\|f\|_2^2 = \int_{\mathbb{R}} 1 \to \infty.$$

3. $L^2(X) \subseteq L^1(X) \implies m(X) < \infty$:

4

<!-- page 86 -->

Let $f = \chi_X$, by assumption we can find a constant $M$ such that $\|\chi_X\|_2 \leq M\|\chi_X\|_1$.

Then pick a sequence of sets $E_k \nearrow X$ such that $m(E_k) < \infty$ for all $k$, $\chi_{E_k} \nearrow \chi_X$, and thus $\|\chi_{E_k}\|_p \leq M\|\chi_E\|_p$. By the lemma, $\|\chi_{E_k}\|_p = m(E_k)^{1/p}$, so we have

$$\begin{array}{l} \|\chi_{E_k}\|_2 \leq M\|\chi_{E_k}\|_1 \implies \frac{\|\chi_{E_k}\|_2}{\|\chi_{E_k}\|_1} \leq M \\ \implies \frac{m(E_k)^{1/2}}{m(E_k)} \leq M \\ \implies m(E_k)^{-1/2} \leq M \\ \implies m(E_k) \leq M^2 < \infty. \end{array}$$

and by continuity of measure, we have $\lim_K m(E_k) = m(X) \leq M^2 < \infty$. $\square$

## 2.2 Part b

1. $L_1(X) \cap L^\infty(X) \subset L^2(X)$:

Let $f \in L^1(X) \cap L^\infty(X)$ and $M := \|f\|_\infty$, then

$$\|f\|_2^2 = \int_X |f|^2 = \int_X |f||f| \leq \int_X M|f| = M \int |f| := \|f\|_\infty \|f\|_1 < \infty. \tag{1}$$

The inclusion is strict, since we know from above that there is a function in $L^2(X)$ that is not in $L^\infty(X)$.

Note that taking square roots in (1) immediately yields

$$\|f\|_{L^2(X)} \leq \|f\|_{L^1(X)}^{1/2} \|f\|_{L^\infty(X)}^{1/2}.$$

2. $L^2(X) \subset L^1(X) + L^\infty(X)$:

Let $f \in L^2(X)$, then write $S = \{x \ni |f(x)| \geq 1\}$ and $f = \chi_S f + \chi_{S^c} f := g + h$.

Since $x \geq 1 \implies x^2 \geq x$, we have

$$\|g\|_1^2 = \int_X |g| = \int_S |f| \leq \int_S |f|^2 \leq \int_X |f|^2 = \|f\|_2^2 < \infty,$$

and so $g \in L^1(X)$.

To see that $h \in L^\infty(X)$, we just note that $h$ is bounded by 1 by construction, and so $\|h\|_\infty \leq 1 < \infty$.

## 3 Problem 3

For notational convenience, it suffices to prove this for $\ell^p(\mathbb{N})$, where we re-index each sequence in $\ell^p(\mathbb{Z})$ using a bijection $\mathbb{Z} \to \mathbb{N}$.

Note: this technically reorders all sums appearing, but since we are assuming absolute convergence everywhere, this can be done. One can also just replace $\sum_{j=n}^m |a_j|^p$ with $\sum_{n \leq |j| \leq m} |a_j|^p$ in what follows.

5

<!-- page 87 -->

1. $\ell^1(\mathbb{N}) \subset \ell^2(\mathbb{N})$:

Suppose $\sum_j |a|_j < \infty$, then its tails go to zero, so choose $N$ large enough so that

$$j \ge N \implies |a_j| < 1.$$

But then

$$j \ge N \implies |a_j|^2 < |a_j|,$$

and

$$\begin{aligned} \sum_j |a_j|^2 &= \sum_{j=1}^N |a_j|^2 + \sum_{j=N+1}^\infty |a_j|^2 \\ &\le \sum_{j=1}^N |a_j|^2 + \sum_{j=N+1}^\infty |a_j| \\ &\le M + \sum_{j=N+1}^\infty |a_j| \\ &\le M + \sum_{j=1}^\infty |a_j| \\ &< \infty. \end{aligned}$$

where we just note that the first portion of the sum is a finite sum of finite numbers and thus bounded.

To see that the inclusion is strict, take $\mathbf{a} := \{j^{-1}\}_{j=1}^\infty$; then $\|\mathbf{a}\|_2 < \infty$ by the $p$-test by $\|\mathbf{a}\|_1 = \infty$ since it yields the harmonic series.

2. $\ell^2(\mathbb{N}) \subset \ell^\infty(\mathbb{N})$:

This follows from the contrapositive: if $\mathbf{a}$ is a sequence with unbounded terms, then $\|\mathbf{a}\|_2 = \sum |a_j|^2$ can not be finite, since convergence would require that $|a_j|^2 \to 0$ and thus $|a_j| \to 0$.

To see that the inclusion is strict, take $\mathbf{a} = \{1\}_{j=1}^\infty$. Then $\|\mathbf{a}\|_\infty = 1$, but the corresponding sum does not converge.

3. $\|\mathbf{a}\|_2 \le \|\mathbf{a}\|_1$:

Let $M = \|\mathbf{a}\|_1$, then

$$\|\mathbf{a}\|_2^2 \le \|\mathbf{a}\|_1^2 \iff \frac{\|\mathbf{a}\|_2^2}{M^2} \le 1 \iff \sum_j \left|\frac{a_j}{M}\right|^2 \le 1.$$

But then we can use the fact that

$$\left|\frac{a_j}{M}\right| \le 1 \implies \left|\frac{a_j}{M}\right|^2 \le \left|\frac{a_j}{M}\right|$$

6

<!-- page 88 -->

to obtain

$$\sum_{j} \left| \frac{a_{j}}{M} \right|^{2} \leq \sum_{j} \left| \frac{a_{j}}{M} \right| = \frac{1}{M} \sum_{j} |a_{j}| := 1.$$

4. $\|\mathbf{a}\|_{\infty} \leq \|\mathbf{a}\|_{2}$:

This follows from the fact that, we have

$$\|\mathbf{a}\|_{\infty}^{2} := \left( \sup_{j} |a_{j}| \right)^{2} = \sup_{j} |a_{j}|^{2} \leq \sum_{j} |a_{j}|^{2} = \|\mathbf{a}\|_{2}^{2}$$

and taking square roots yields the desired inequality.

Note: the middle inequality follows from the fact that the supremum $S$ is the least upper bound of all of the $a_{j}$, so for all $j$, we have $a_{j} + \varepsilon > S$ for every $\varepsilon > 0$. But in particular, $a_{k} + a_{j} > a_{j}$ for any pair $a_{j}, a_{k}$ where $a_{k} \neq 0$, so $a_{k} + a_{j} > S$ and thus so is the entire sum.

## 4 Problem 4

### 4.1 Part a

Let $\{f_{k}\}$ be a Cauchy sequence, then $\|f_{k} - f_{j}\|_{u} \to 0$. Define a candidate limit by fixing $x$, then using the fact that $|f_{j}(x) - f_{k}(x)| \to 0$ as a Cauchy sequence in $\mathbb{R}$, which converges to some $f(x)$.

We want to show that and $\|f_{n} - f\|_{u} \to 0$ and $f \in C([0, 1])$.

This is immediate though, since $f_{n} \to f$ uniformly by construction, and the uniform limit of continuous functions is continuous.

### 4.2 Part b

It suffices to produce a Cauchy sequence of continuous functions $f_{k}$ such that $\|f_{j} - f_{j}\|_{1} \to 0$ but if we define $f(x) := \lim f_{k}(x)$, we have either $\|f\|_{1} = \infty$ or $f$ is not continuous.

To this end, take $f_{k}(x) = x^{k}$ for $k = 1, 2, \cdots, \infty$.

Then pointwise we have

$$f_{k} \to \begin{cases} 0 & x \in [0, 1) \\ 1 & x = 1 \end{cases},$$

which has a clear discontinuity, but

$$\|f_{k} - f_{j}\|_{1} := \int_{0}^{1} x^{k} - x^{j} = \frac{1}{k+1} - \frac{1}{j+1} \to 0.$$

7

<!-- page 89 -->

# 5 Problem 5

## 5.1 Part a

$\Longleftarrow$ : It suffices to show that the map

$$\begin{array}{l} H \twoheadrightarrow \ell^2(\mathbb{N}) \\ \mathbf{x} \mapsto \{\langle \mathbf{x}, \mathbf{u}_n \rangle\}_{n=1}^\infty := \{a_n\}_{n=1}^\infty \end{array}$$

is a surjection, and for every $\mathbf{a} \in \ell^2(\mathbb{N})$, we can pull back to some $\mathbf{x} \in H$ such that $\|\mathbf{x}\|_H = \|\mathbf{a}\|_{\ell^2(\mathbb{N})}$.

Following the proof in Neil's notes, let $\mathbf{a} \in \ell^2(\mathbb{N})$ be given by $\mathbf{a} = \{a_j\}$, and define $S_N = \sum_{n=1}^N a_n \mathbf{u}_n$. We then have

$$\begin{array}{l} \|S_N - S_M\|_H = \left\| \sum_{n=M+1}^N a_n \mathbf{u}_n \right\|_H \\ = \sum_{n=M+1}^N \|a_n \mathbf{u}_n\|_H \quad \text{by Pythagoras, since the } \mathbf{u}_n \text{ are orthogonal} \\ = \sum_{n=M+1}^N |a_n|_\mathbb{C} \|\mathbf{u}_n\|_H \\ = \sum_{n=M+1}^N |a_n|_\mathbb{C} \quad \text{since the } \mathbf{u}_n \text{ are orthonormal} \\ \to 0 \quad \text{as } N, M \to \infty, \end{array}$$

which goes to zero because it is the tail of a convergent sum in $\mathbb{R}$.

Since $H$ is complete, every Cauchy sequence converges, and in particular $S_N \to \mathbf{x} \in H$ for some $\mathbf{x}$. We now have

$$\begin{array}{l} |\langle \mathbf{x}, \mathbf{u}_n \rangle| = |\langle \mathbf{x} - S_N + S_N, \mathbf{u}_n \rangle| \quad \forall n, N \\ = |\langle \mathbf{x} - S_N, \mathbf{u}_n \rangle + \langle S_N, \mathbf{u}_n \rangle| \quad \forall n, N \\ \leq \|\mathbf{x} - S_N\|_H \|\mathbf{u}_n\|_H + |\langle S_N, \mathbf{u}_n \rangle| \quad \forall n, N \text{ by Cauchy-Schwartz} \\ = \|\mathbf{x} - S_N\|_H + |\langle S_N, \mathbf{u}_n \rangle| \quad \forall n, N \\ = \|\mathbf{x} - S_N\|_H + |a_n| \quad \forall N \geq n \\ \to 0 + |a_n| \quad \text{as } N \to \infty, \end{array}$$

where we just note that

$$\langle S_N, \mathbf{u}_n \rangle = \left\langle \sum_{j=1}^N a_j \mathbf{u}_j, \mathbf{u}_n \right\rangle = \sum_{j=1}^N a_j \langle \mathbf{u}_j, \mathbf{u}_n \rangle = a_n \iff N \geq n$$

8

<!-- page 90 -->

since $\langle \mathbf{u}_j, \mathbf{u}_n \rangle = \delta_{j,n}$ and so the $a_n$ term is extracted iff $\mathbf{u}_n$ actually appears as a summand.

We thus have

$$\langle \mathbf{x}, \mathbf{u}_n \rangle = |a_n| \quad \forall n,$$

and since $\{\mathbf{u}_n\}$ is a basis, we can apply Parseval's identity to obtain

$$\|\mathbf{x}\|_H^2 = \sum_{n=1}^\infty |\langle \mathbf{x}, \mathbf{u}_n \rangle| := \sum_{n=1}^\infty |a_n|.$$

$\implies$ : Given a vector $\mathbf{x} = \sum_n a_n \mathbf{u}_n$, we can immediately note that both $\|\mathbf{x}\|_H < \infty$ and $\langle \mathbf{x}, \mathbf{u}_n \rangle = a_n$. Since $\{\mathbf{u}_n\}$ being a basis is equivalent to Parseval's identity holding, we immediately obtain

$$\sum_{n=1}^\infty |a_n| = \sum_{n=1}^\infty |\langle \mathbf{x}, \mathbf{u}_n \rangle| = \|\mathbf{x}\|_H^2 < \infty.$$

## 5.2 Part b

In both cases, suppose such a linear functional exists.

1. Using part (a), we know that $H$ is isometrically isomorphic to $\ell^2(\mathbb{N})$, and thus $H_f^\vee \cong (\ell^2(\mathbb{N}))^\vee \cong_d \ell^2(\mathbb{N})$.

Note: this follows since $\ell^p(\mathbb{N})^\vee \cong \ell^q(\mathbb{N})$ where $p, q$ are Holder conjugates.

But then, since $L \in H^\vee$, under the isometry $f$ it maps to the functional

$$L_\ell : \ell^2(\mathbb{Z}) \to \mathbb{C}$$

$$\mathbf{a} = \{a_n\} \mapsto \sum_{n \in \mathbb{N}} a_n n^{-1},$$

which under the identification of dual spaces $g$ identifies $L_\ell$ with the vector $\mathbf{b} := \{n^{-1}\}_{n \in \mathbb{N}}$.

Most importantly, these are all isometries, so we have the equalities

$$\|L\|_H = \|L_\ell\|_{\ell^2(\mathbb{N})^\vee} = \|\mathbf{b}\|_{\ell^2(\mathbb{N})},$$

so it suffices to compute the $\ell^2$ norm of the sequence $b_n = \frac{1}{n}$. To this end, we have

$$\begin{aligned} \|\mathbf{b}\|_{\ell^2(\mathbb{N})}^2 &= \sum_n \left| \frac{1}{n} \right|^2 \\ &= \sum_n \frac{1}{n^2} \\ &= \frac{\pi^2}{6}, \end{aligned}$$

which shows that $\|L\|_H = \pi/\sqrt{6}$.

9

<!-- page 91 -->

2. Using the same argument, we obtain $\mathbf{b} = \left\{n^{-1/2}\right\}_{n \in \mathbb{N}}$, and thus

$$\|L\|_H^2 = \|\mathbf{b}\|_{\ell^2(\mathbb{N})}^2 = \sum_n \left| n^{-1/2} \right|^2 \to \infty.$$

which shows that $L$ is unbounded, and thus can not be a continuous linear functional. $\square$

## 6 Problem 6

We can use the fact that $\Lambda_p \in (L^p)^\vee \cong L^q$, where this is an isometric isomorphism given by the map

$$I : L^q \to (L^p)^\vee$$

$$g \mapsto (f \mapsto \int fg).$$

Under this identification, for any $\Lambda \in (L^p)^\vee$, to any $\Lambda \in (L^p)^\vee$ we can associate a $g \in L^q$, where we have

$$\|\Lambda\|_{(L^p)^\vee} = \|g\|_{L^q}.$$

In this case, we can identify $\Lambda_p = I(g)$, where $g(x) = x^2$ and we can verify that $g \in L^q$ by computing its norm:

$$\|g\|_{L^q}^q = \int_0^1 (x^2)^q \, dx$$

$$= \left. \frac{x^{2q+1}}{2q+1} \right|_0^1$$

$$= \frac{1}{2q+1}$$

$$= \frac{p-1}{3p-1} < \infty,$$

where we identify $q = \frac{p}{p-1}$, and note that this is finite for all $1 \le p \le \infty$ since it limits to $\frac{1}{3}$. But then

$$\|\Lambda_p\|_{(L^p)^\vee} = \|g\|_{L^q} = \left( \frac{p-1}{3p-1} \right)^{\frac{1}{q}} = \left( \frac{p-1}{3p-1} \right)^{\frac{p-1}{p}},$$

which shows that $\Lambda_p$ is bounded and thus a continuous linear functional. $\square$

10
