/**
 * Pac-Man Intelligent Search - Complete Team Demonstration UI & Architecture Dashboard
 * Module: SE3062 / IT3012 - Intelligent Systems (SLIIT)
 * Lecturer: Mr. Jeewaka Perera
 * Team Members:
 *  - Member 1: S.P.R.H. Wijesiri (IT24100602) - Q1 (DFS) & Q5 (Corners Problem)
 *  - Member 2: Atheek Fareez (IT24103933)    - Q2 (BFS) & Q3 (UCS)
 *  - Member 3: Wazni Ahamed (IT24103352)     - Q4 (A*) & Q5 (Corners State Space)
 *  - Member 4: Raashidh Rizvi (IT24104191)   - Q6 (Corners Heuristic) & Q7 (Food Heuristic)
 */

document.addEventListener('DOMContentLoaded', () => {
  // =========================================================================
  // 1. TEAM ROSTER & MEMBER KNOWLEDGE PROFILES
  // =========================================================================
  const teamProfiles = {
    all: {
      name: "All Team Members",
      id: "4 Developers • Questions Q1 - Q7",
      role: "SLIIT Intelligent Systems",
      greeting: "Pac-Man Search Architecture & Team Defense",
      subtitle: "Comprehensive 4-Member Project Walkthrough (SE3062 / IT3012)",
      status: "Team Project: 100% Viva Ready",
      highlightAlgo: "bfs",
      nodes: ["node-engine", "node-agent", "node-pos", "node-corners", "node-food", "node-dfs", "node-bfs", "node-ucs", "node-astar", "node-util", "node-heuristics"],
      metrics: {
        val1: "7 / 7", lbl1: "Total Questions Implemented", b1: "4 Developers", s1: "Modular architecture",
        val2: "68", lbl2: "MediumMaze Optimal Steps", b2: "BFS & UCS", s2: "vs DFS 146 nodes",
        val3: "< 1,200", lbl3: "Heuristic Efficiency (Q6 & Q7)", b3: "Full 8/8 Threshold", s3: "Admissible & Consistent",
        val4: "100%", lbl4: "Autograder Pass Rate", b4: "All Tests Passing", s4: "Zero autograder penalties"
      }
    },
    m1: {
      name: "S.P.R.H. Wijesiri",
      id: "IT24100602 • Member 1",
      role: "DFS & Problem Modeling Lead",
      greeting: "Member 1 Focus: S.P.R.H. Wijesiri",
      subtitle: "Q1 Depth-First Search (search.py) & Q5 Corners Problem (searchAgents.py)",
      status: "Member 1: Q1 & Q5 Verified",
      highlightAlgo: "dfs",
      nodes: ["node-dfs", "node-corners", "node-util"],
      metrics: {
        val1: "Q1 & Q5", lbl1: "Assigned Questions", b1: "DFS & Corners", s1: "search.py & searchAgents.py",
        val2: "146", lbl2: "DFS MediumMaze Expansions", b2: "Path Cost: 130", s2: "LIFO non-optimal",
        val3: "util.Stack", lbl3: "Primary Data Structure", b3: "LIFO Policy", s3: "Graph search cycle check",
        val4: "6 / 6", lbl4: "Autograder Points", b4: "Q1: 3/3 • Q5: 3/3", s4: "Full autograder score"
      }
    },
    m2: {
      name: "Atheek Fareez",
      id: "IT24103933 • Member 2",
      role: "BFS & UCS Algorithm Lead",
      greeting: "Member 2 Focus: Atheek Fareez",
      subtitle: "Q2 Breadth-First Search & Q3 Uniform Cost Search (search.py)",
      status: "Member 2: Q2 & Q3 Verified (8/8)",
      highlightAlgo: "ucs",
      nodes: ["node-bfs", "node-ucs", "node-util"],
      metrics: {
        val1: "Q2 & Q3", lbl1: "Assigned Questions", b1: "BFS & UCS", s1: "search.py implementation",
        val2: "68", lbl2: "MediumMaze Nodes Expanded", b2: "Optimal Path: 68", s2: "Fewest steps & least cost",
        val3: "100%", lbl3: "UCS Cost Optimality", b3: "Dequeue Goal Test", s3: "util.PriorityQueue",
        val4: "8 / 8", lbl4: "Autograder Points", b4: "Q2: 4/4 • Q3: 4/4", s4: "Full autograder marks"
      }
    },
    m3: {
      name: "Wazni Ahamed",
      id: "IT24103352 • Member 3",
      role: "A* & Problem State Lead",
      greeting: "Member 3 Focus: Wazni Ahamed",
      subtitle: "Q4 A* Search (search.py) & Q5 Corners State Space (searchAgents.py)",
      status: "Member 3: Q4 & Q5 Verified",
      highlightAlgo: "astar",
      nodes: ["node-astar", "node-corners", "node-heuristics"],
      metrics: {
        val1: "Q4 & Q5", lbl1: "Assigned Questions", b1: "A* & Corners State", s1: "search.py & searchAgents.py",
        val2: "54", lbl2: "A* MediumMaze Nodes", b2: "Optimal Path: 68", s2: "Lowest expansions",
        val3: "f = g + h", lbl3: "Evaluation Function", b3: "util.PriorityQueue", s3: "Admissible guidance",
        val4: "6 / 6", lbl4: "Autograder Points", b4: "Q4: 3/3 • Q5: 3/3", s4: "Full autograder marks"
      }
    },
    m4: {
      name: "Raashidh Rizvi",
      id: "IT24104191 • Member 4",
      role: "Heuristic & Optimization Lead",
      greeting: "Member 4 Focus: Raashidh Rizvi",
      subtitle: "Q6 Corners Heuristic & Q7 Food Search Heuristic (searchAgents.py)",
      status: "Member 4: Q6 & Q7 Verified",
      highlightAlgo: "astar",
      nodes: ["node-heuristics", "node-food", "node-corners"],
      metrics: {
        val1: "Q6 & Q7", lbl1: "Assigned Questions", b1: "Heuristics Lead", s1: "searchAgents.py",
        val2: "< 1,200", lbl2: "Q6 Nodes Expanded", b2: "Full 8/8 Marks", s2: "mediumCorners benchmark",
        val3: "< 9,000", lbl3: "Q7 Nodes Expanded", b3: "Full 8/8 Marks", s3: "trickySearch benchmark",
        val4: "8 / 8", lbl4: "Autograder Thresholds", b4: "Admissible & Consistent", s4: "Zero overestimations"
      }
    }
  };

  // Node details mapping for architecture inspector
  const nodeData = {
    engine: {
      title: "Game Engine (pacman.py & game.py) — Shared Infrastructure",
      icon: "🎮",
      desc: "Controls the main simulation loop, maze geometry, food positions, ghost dynamics, and score. Sends current GameState to SearchAgent and executes the returned action plan step-by-step.",
      tags: ["Developer: Shared Core", "GameState", "Maze Layout", "Action Execution", "Score Calculation"]
    },
    agent: {
      title: "SearchAgent (searchAgents.py) — Agent Controller",
      icon: "🤖",
      desc: "Instantiates the specific SearchProblem from GameState, invokes the selected algorithm from search.py, retrieves the plan (list of actions), and feeds actions one by one to the Game Engine.",
      tags: ["Developer: Shared Core", "Problem Factory", "Plan Execution", "searchAgents.py"]
    },
    pos: {
      title: "PositionSearchProblem — Single Goal Search",
      icon: "📍",
      desc: "Navigation where state is simply a coordinate (x, y). Defines getStartState(), isGoalState(state), and getSuccessors(state) returning [(nextState, action, stepCost)].",
      tags: ["Developer: Shared Core", "State: (x, y)", "Unit Step Cost = 1", "searchAgents.py"]
    },
    corners: {
      title: "CornersProblem (Q5) — S.P.R.H. Wijesiri (M1) & Wazni Ahamed (M3)",
      icon: "📐",
      desc: "Pac-Man must visit all four corners of the maze. The state must be a compact, hashable tuple: ((x, y), (visitedNW, visitedNE, visitedSW, visitedSE)). Tested by python autograder.py -q q5.",
      tags: ["Developer: M1 (Wijesiri) & M3 (Wazni)", "Q5 Implementation", "State: (pos, cornersTuple)", "Hashable Immutable Tuple"]
    },
    food: {
      title: "FoodSearchProblem (Q7) — Raashidh Rizvi (M4)",
      icon: "🍒",
      desc: "Pac-Man must eat all remaining food dots. State space size is huge: (position * 2^foodCount). Requires sophisticated admissible heuristics (MST / bounding) to solve within autograder thresholds.",
      tags: ["Developer: Raashidh Rizvi (M4)", "Q7 Implementation", "State: (pos, foodGrid)", "Heuristic Search"]
    },
    dfs: {
      title: "Depth-First Search (DFS - Q1) — S.P.R.H. Wijesiri (M1)",
      icon: "🌲",
      desc: "Explores the deepest node in the search tree using a LIFO Stack from util.py. Complete in finite graphs with closed set visited tracking, but NOT optimal (takes 130 steps on MediumMaze vs optimal 68).",
      tags: ["Developer: S.P.R.H. Wijesiri (M1)", "Data Structure: util.Stack (LIFO)", "Completeness: Finite Graphs", "Optimal: No"]
    },
    bfs: {
      title: "Breadth-First Search (BFS - Q2) — Atheek Fareez (M2)",
      icon: "🌊",
      desc: "Expands the shallowest node in the frontier using util.Queue (FIFO). Guarantees optimal path length (fewest steps) when all step costs are equal. Solves MediumMaze in 68 expanded nodes and 68 actions. Score: 4/4.",
      tags: ["Developer: Atheek Fareez (M2)", "Data Structure: util.Queue (FIFO)", "Optimal: Yes (Unit Cost)", "68 Nodes Expanded"]
    },
    ucs: {
      title: "Uniform Cost Search (UCS - Q3) — Atheek Fareez (M2)",
      icon: "⚖️",
      desc: "Expands the node with lowest cumulative path cost g(n) using util.PriorityQueue. Critically, goal testing is performed upon DEQUEUE (not enqueue) to guarantee optimal solutions across arbitrary positive step costs. Score: 4/4.",
      tags: ["Developer: Atheek Fareez (M2)", "Priority: lowest g(n)", "util.PriorityQueue", "Optimal: Yes (Any Positive Cost)"]
    },
    astar: {
      title: "A* Search (AStar - Q4) — Wazni Ahamed (M3)",
      icon: "🌟",
      desc: "Informed graph search ordering the frontier by f(n) = g(n) + h(n), balancing backward cost g(n) and forward heuristic h(n). Expands only 54 nodes on MediumMaze with Manhattan heuristic. Score: 3/3.",
      tags: ["Developer: Wazni Ahamed (M3)", "Evaluation: f(n) = g(n) + h(n)", "util.PriorityQueue", "Optimal: Yes (Consistent h)"]
    },
    util: {
      title: "Supporting Data Structures (util.py) — Shared ADT Library",
      icon: "🧰",
      desc: "Provides standardized implementations of fundamental search structures: Stack (for DFS - M1), Queue (for BFS - M2), and PriorityQueue (for UCS - M2, and A* - M3).",
      tags: ["Developer: Shared Core", "Stack (LIFO)", "Queue (FIFO)", "PriorityQueue (Min-Heap)"]
    },
    heuristics: {
      title: "Heuristics (cornersHeuristic & foodHeuristic) — Raashidh Rizvi (M4)",
      icon: "🎯",
      desc: "Domain-specific guidance functions estimating remaining distance. CornersHeuristic solves mediumCorners in < 1,200 nodes (8/8). FoodHeuristic solves trickySearch in < 9,000 nodes (8/8). Must be admissible & consistent.",
      tags: ["Developer: Raashidh Rizvi (M4)", "Q6 & Q7 Lead", "Admissibility: h(n) <= h*(n)", "Consistency Triangle Inequality"]
    }
  };

  // =========================================================================
  // 2. MEMBER SWITCHER & DASHBOARD TELEMETRY UPDATER
  // =========================================================================
  let currentMember = "all";

  const memberButtons = document.querySelectorAll('.member-pill-btn[data-member]');
  const teamMemberCards = document.querySelectorAll('.team-member-card');
  const sbRoleTitle = document.getElementById('sbRoleTitle');
  const sbMemberName = document.getElementById('sbMemberName');
  const sbMemberId = document.getElementById('sbMemberId');
  const sbMemberTag = document.getElementById('sbMemberTag');
  const headerGreeting = document.getElementById('headerGreeting');
  const headerSubtitle = document.getElementById('headerSubtitle');
  const headerProjectStatus = document.getElementById('headerProjectStatus');

  const metricValue1 = document.getElementById('metricValue1');
  const metricLabel1 = document.getElementById('metricLabel1');
  const metricBadge1 = document.getElementById('metricBadge1');
  const metricSubtext1 = document.getElementById('metricSubtext1');

  const metricValue2 = document.getElementById('metricValue2');
  const metricLabel2 = document.getElementById('metricLabel2');
  const metricBadge2 = document.getElementById('metricBadge2');
  const metricSubtext2 = document.getElementById('metricSubtext2');

  const metricValue3 = document.getElementById('metricValue3');
  const metricLabel3 = document.getElementById('metricLabel3');
  const metricBadge3 = document.getElementById('metricBadge3');
  const metricSubtext3 = document.getElementById('metricSubtext3');

  const metricValue4 = document.getElementById('metricValue4');
  const metricLabel4 = document.getElementById('metricLabel4');
  const metricBadge4 = document.getElementById('metricBadge4');
  const metricSubtext4 = document.getElementById('metricSubtext4');

  const simMemberAttribution = document.getElementById('simMemberAttribution');
  const algoSelect = document.getElementById('algoSelect');

  function applyMemberFocus(memberKey) {
    currentMember = memberKey;
    const profile = teamProfiles[memberKey] || teamProfiles.all;

    // 1. Update button states
    memberButtons.forEach(btn => {
      btn.classList.toggle('active', btn.dataset.member === memberKey);
    });

    // 2. Update team card selection
    teamMemberCards.forEach(card => {
      card.classList.toggle('active-selected', card.dataset.member === memberKey);
    });

    // 3. Update Sidebar & Header
    sbMemberName.textContent = profile.name;
    sbMemberId.textContent = profile.id;
    sbRoleTitle.textContent = profile.role;
    sbMemberTag.textContent = memberKey === 'all' ? "SLIIT Intelligent Systems" : "Active Member Focus";

    headerGreeting.textContent = profile.greeting;
    headerSubtitle.textContent = profile.subtitle;
    headerProjectStatus.textContent = profile.status;

    // 4. Update Metric Cards
    metricValue1.innerHTML = `${profile.metrics.val1} <span style="font-size: 16px; font-weight: 500; color: var(--text-muted);">${profile.metrics.b1}</span>`;
    metricLabel1.textContent = profile.metrics.lbl1;
    metricBadge1.textContent = profile.metrics.b1;
    metricSubtext1.textContent = profile.metrics.s1;

    metricValue2.innerHTML = `${profile.metrics.val2} <span style="font-size: 16px; font-weight: 500; color: var(--text-muted);">Nodes/Steps</span>`;
    metricLabel2.textContent = profile.metrics.lbl2;
    metricBadge2.textContent = profile.metrics.b2;
    metricSubtext2.textContent = profile.metrics.s2;

    metricValue3.innerHTML = `${profile.metrics.val3} <span style="font-size: 16px; font-weight: 500; color: var(--text-muted);">Metric</span>`;
    metricLabel3.textContent = profile.metrics.lbl3;
    metricBadge3.textContent = profile.metrics.b3;
    metricSubtext3.textContent = profile.metrics.s3;

    metricValue4.innerHTML = `${profile.metrics.val4} <span style="font-size: 16px; font-weight: 500; color: #10b981;">Score</span>`;
    metricLabel4.textContent = profile.metrics.lbl4;
    metricBadge4.textContent = profile.metrics.b4;
    metricSubtext4.textContent = profile.metrics.s4;

    // 5. Highlight corresponding nodes in architecture diagram
    document.querySelectorAll('.sys-node').forEach(node => {
      node.classList.remove('active-highlight');
    });

    if (profile.nodes && profile.nodes.length > 0) {
      profile.nodes.forEach(id => {
        const el = document.getElementById(id);
        if (el) el.classList.add('active-highlight');
      });
      // Click first node to populate inspector
      const firstNode = document.getElementById(profile.nodes[0]);
      if (firstNode) firstNode.click();
    }

    // 6. Sync Pathfinding Simulator Algorithm
    if (profile.highlightAlgo) {
      algoSelect.value = profile.highlightAlgo;
      updateSimulatorAttribution();
      initSearch();
    }

    // 7. Filter Viva Cards automatically
    filterVivaCards(memberKey);
  }

  function updateSimulatorAttribution() {
    const val = algoSelect.value;
    if (val === 'dfs') {
      simMemberAttribution.textContent = "Active Algorithm: DFS (Q1) • Lead: S.P.R.H. Wijesiri (Member 1)";
    } else if (val === 'bfs') {
      simMemberAttribution.textContent = "Active Algorithm: BFS (Q2) • Lead: Atheek Fareez (Member 2)";
    } else if (val === 'ucs') {
      simMemberAttribution.textContent = "Active Algorithm: UCS (Q3) • Lead: Atheek Fareez (Member 2)";
    } else if (val === 'astar') {
      simMemberAttribution.textContent = "Active Algorithm: A* (Q4) • Lead: Wazni Ahamed (Member 3)";
    }
  }

  // =========================================================================
  // VIVA DEFENSE FLASHCARD FILTERING & CONTROLS
  // =========================================================================
  const vivaCards = document.querySelectorAll('.viva-card');
  const vivaFilterButtons = document.querySelectorAll('[data-viva-filter]');
  const btnToggleAllViva = document.getElementById('btnToggleAllViva');
  let allVivaExpanded = false;

  function filterVivaCards(memberKey) {
    // 1. Update filter button active states
    vivaFilterButtons.forEach(btn => {
      btn.classList.toggle('active', btn.dataset.vivaFilter === memberKey);
    });

    // 2. Filter visibility of cards
    vivaCards.forEach(card => {
      const cardMember = card.dataset.member;
      if (memberKey === 'all' || cardMember === memberKey) {
        card.style.display = 'flex';
      } else {
        card.style.display = 'none';
      }
    });
  }

  vivaFilterButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      const filterKey = btn.dataset.vivaFilter;
      filterVivaCards(filterKey);
    });
  });

  if (btnToggleAllViva) {
    btnToggleAllViva.addEventListener('click', () => {
      allVivaExpanded = !allVivaExpanded;
      vivaCards.forEach(card => {
        if (card.style.display !== 'none') {
          card.classList.toggle('expanded', allVivaExpanded);
        }
      });
      btnToggleAllViva.textContent = allVivaExpanded ? '📕 Collapse All' : '📖 Expand All';
    });
  }

  memberButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      applyMemberFocus(btn.dataset.member);
    });
  });

  teamMemberCards.forEach(card => {
    card.addEventListener('click', () => {
      applyMemberFocus(card.dataset.member);
    });
  });

  // =========================================================================
  // 3. ARCHITECTURE DIAGRAM INSPECTOR
  // =========================================================================
  const sysNodes = document.querySelectorAll('.sys-node');
  const inspectorDrawer = document.getElementById('inspectorDrawer');
  const inspectorTitle = document.getElementById('inspectorTitle');
  const inspectorDesc = document.getElementById('inspectorDesc');
  const inspectorTags = document.getElementById('inspectorTags');
  const inspectorIcon = document.getElementById('inspectorIcon');

  sysNodes.forEach(node => {
    node.addEventListener('click', () => {
      document.querySelectorAll('.sys-node').forEach(n => n.classList.remove('active-highlight'));
      node.classList.add('active-highlight');

      const key = node.dataset.node;
      const data = nodeData[key];
      if (!data) return;

      inspectorIcon.textContent = data.icon;
      inspectorTitle.textContent = data.title;
      inspectorDesc.textContent = data.desc;
      inspectorTags.innerHTML = data.tags.map(t => `<span class="tag-pill">${t}</span>`).join('');

      inspectorDrawer.style.animation = 'none';
      inspectorDrawer.offsetHeight;
      inspectorDrawer.style.animation = 'fadeIn 0.3s ease';
    });
  });


  // =========================================================================
  // 5. SIDEBAR NAVIGATION
  // =========================================================================
  const navLinks = document.querySelectorAll('.nav-item');
  navLinks.forEach(link => {
    link.addEventListener('click', () => {
      navLinks.forEach(l => l.classList.remove('active'));
      link.classList.add('active');
    });
  });

  // =========================================================================
  // 6. INTERACTIVE MAZE PATHFINDING SIMULATOR
  // =========================================================================
  const canvas = document.getElementById('mazeCanvas');
  const ctx = canvas.getContext('2d');

  const mazeSelect = document.getElementById('mazeSelect');
  const btnPlay = document.getElementById('btnPlay');
  const btnStep = document.getElementById('btnStep');
  const btnReset = document.getElementById('btnReset');
  const speedSlider = document.getElementById('speedSlider');
  const playIcon = document.getElementById('playIcon');
  const playText = document.getElementById('playText');

  const statExpanded = document.getElementById('statExpanded');
  const statFrontier = document.getElementById('statFrontier');
  const statCost = document.getElementById('statCost');
  const frontierVisualList = document.getElementById('frontierVisualList');
  const executionLog = document.getElementById('executionLog');
  const simStatusBadge = document.getElementById('simStatusBadge');
  const dataStructureName = document.getElementById('dataStructureName');

  const mazes = {
    medium: {
      cols: 28, rows: 17,
      start: { x: 1, y: 1 },
      goal: { x: 26, y: 15 },
      grid: [
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,0,0,0,0,0,0,1,0,0,0,0,0,1,1,0,0,0,0,0,1,0,0,0,0,0,0,1],
        [1,0,1,1,1,1,0,1,0,1,1,1,0,1,1,0,1,1,1,0,1,0,1,1,1,1,0,1],
        [1,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,1],
        [1,0,1,0,1,1,1,1,1,1,0,1,1,1,1,1,1,0,1,1,1,1,1,1,0,1,0,1],
        [1,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,1],
        [1,1,1,0,1,0,1,1,0,1,1,1,1,0,0,1,1,1,1,0,1,1,0,1,0,1,1,1],
        [1,0,0,0,0,0,1,1,0,0,0,0,1,0,0,1,0,0,0,0,1,1,0,0,0,0,0,1],
        [1,0,1,1,1,0,1,1,1,1,1,0,1,0,0,1,0,1,1,1,1,1,0,1,1,1,0,1],
        [1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1],
        [1,1,1,0,1,0,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,0,1,0,1,1,1],
        [1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1],
        [1,0,1,1,1,1,1,0,1,1,1,0,1,1,1,1,0,1,1,1,0,1,1,1,1,1,0,1],
        [1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1],
        [1,1,1,0,1,1,1,0,1,0,1,1,1,1,1,1,1,1,0,1,0,1,1,1,0,1,1,1],
        [1,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
      ]
    },
    small: {
      cols: 16, rows: 10,
      start: { x: 1, y: 1 },
      goal: { x: 14, y: 8 },
      grid: [
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,0,0,0,1,0,0,0,0,0,0,1,0,0,0,1],
        [1,0,1,0,1,0,1,1,1,1,0,1,0,1,0,1],
        [1,0,1,0,0,0,1,0,0,1,0,0,0,1,0,1],
        [1,0,1,1,1,0,1,0,0,1,0,1,1,1,0,1],
        [1,0,0,0,1,0,0,0,0,0,0,1,0,0,0,1],
        [1,1,1,0,1,1,1,0,0,1,1,1,0,1,1,1],
        [1,0,0,0,0,0,1,0,0,1,0,0,0,0,0,1],
        [1,0,1,1,1,0,0,0,0,0,0,1,1,1,0,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
      ]
    },
    tiny: {
      cols: 10, rows: 6,
      start: { x: 1, y: 1 },
      goal: { x: 8, y: 4 },
      grid: [
        [1,1,1,1,1,1,1,1,1,1],
        [1,0,0,0,1,0,0,0,0,1],
        [1,1,1,0,1,0,1,1,0,1],
        [1,0,0,0,0,0,0,1,0,1],
        [1,0,1,1,1,1,0,0,0,1],
        [1,1,1,1,1,1,1,1,1,1]
      ]
    }
  };

  let currentMaze = mazes.medium;
  let isRunning = false;
  let timerId = null;

  let frontier = [];
  let visited = new Set();
  let expandedCount = 0;
  let finalPath = null;
  let activeCurrentNode = null;
  let stepLog = [];

  function getManhattan(a, b) {
    return Math.abs(a.x - b.x) + Math.abs(a.y - b.y);
  }

  function stateKey(pos) {
    return `${pos.x},${pos.y}`;
  }

  function initSearch() {
    clearTimeout(timerId);
    isRunning = false;
    playIcon.textContent = "▶";
    playText.textContent = "Start Search";

    const selectedMazeKey = mazeSelect.value;
    currentMaze = mazes[selectedMazeKey] || mazes.medium;

    frontier = [];
    visited = new Set();
    expandedCount = 0;
    finalPath = null;
    activeCurrentNode = null;
    stepLog = [];

    const start = currentMaze.start;
    const goal = currentMaze.goal;
    const algo = algoSelect.value;

    let initPriority = 0;
    if (algo === 'ucs') initPriority = 0;
    if (algo === 'astar') initPriority = getManhattan(start, goal);

    frontier.push({
      state: { x: start.x, y: start.y },
      path: [start],
      cost: 0,
      priority: initPriority
    });

    if (algo === 'bfs') {
      dataStructureName.textContent = "util.Queue (FIFO) [Atheek - M2]";
    } else if (algo === 'dfs') {
      dataStructureName.textContent = "util.Stack (LIFO) [Wijesiri - M1]";
    } else if (algo === 'ucs') {
      dataStructureName.textContent = "util.PriorityQueue (Priority: g(n)) [Atheek - M2]";
    } else if (algo === 'astar') {
      dataStructureName.textContent = "util.PriorityQueue (Priority: g(n) + h(n)) [Wazni - M3]";
    }

    simStatusBadge.textContent = "Initialized";
    simStatusBadge.style.color = "#34d399";
    simStatusBadge.style.background = "rgba(16, 185, 129, 0.12)";

    addLog(`Initialized ${algo.toUpperCase()} search on ${selectedMazeKey} maze.`);
    addLog(`Start Position: (${start.x}, ${start.y}), Goal: (${goal.x}, ${goal.y}).`);

    updateSimulatorAttribution();
    updateTelemetry();
    drawMaze();
  }

  function addLog(msg) {
    stepLog.push(msg);
    if (stepLog.length > 50) stepLog.shift();
    executionLog.innerHTML = stepLog.map(m => `<div>&gt; ${m}</div>`).join('');
    executionLog.scrollTop = executionLog.scrollHeight;
  }

  function updateTelemetry() {
    statExpanded.textContent = expandedCount;
    statFrontier.textContent = frontier.length;
    statCost.textContent = activeCurrentNode ? activeCurrentNode.cost : (finalPath ? finalPath.length - 1 : 0);

    if (frontier.length === 0) {
      frontierVisualList.innerHTML = `<span style="color: var(--text-muted);">[Frontier is Empty]</span>`;
    } else {
      const topItems = frontier.slice(0, 6).map(item => {
        return `[(${item.state.x},${item.state.y}) c=${item.cost}${algoSelect.value === 'astar' ? ` p=${item.priority}` : ''}]`;
      });
      frontierVisualList.innerHTML = topItems.join(' → ') + (frontier.length > 6 ? ` ... +${frontier.length - 6} more` : '');
    }
  }

  function stepSearch() {
    if (finalPath) return false;
    if (frontier.length === 0) {
      simStatusBadge.textContent = "Failed / No Path";
      simStatusBadge.style.color = "#ef4444";
      addLog("Search terminated: Frontier empty without reaching goal.");
      return false;
    }

    const algo = algoSelect.value;
    let node;

    if (algo === 'dfs') {
      node = frontier.pop();
    } else if (algo === 'bfs') {
      node = frontier.shift();
    } else {
      let bestIdx = 0;
      for (let i = 1; i < frontier.length; i++) {
        if (frontier[i].priority < frontier[bestIdx].priority) {
          bestIdx = i;
        }
      }
      node = frontier.splice(bestIdx, 1)[0];
    }

    activeCurrentNode = node;
    const currKey = stateKey(node.state);

    const goal = currentMaze.goal;
    if (node.state.x === goal.x && node.state.y === goal.y) {
      finalPath = node.path;
      simStatusBadge.textContent = "Goal Reached! (Optimal)";
      simStatusBadge.style.color = "#fbbf24";
      addLog(`🎯 GOAL FOUND at (${goal.x}, ${goal.y})! Path Cost: ${node.cost} actions.`);
      addLog(`Summary: Expanded ${expandedCount} nodes. Solution path highlighted.`);
      updateTelemetry();
      drawMaze();
      return false;
    }

    if (visited.has(currKey)) {
      return true;
    }

    visited.add(currKey);
    expandedCount++;

    const dirs = [
      { dx: 0, dy: -1 },
      { dx: 1, dy: 0  },
      { dx: 0, dy: 1  },
      { dx: -1, dy: 0 }
    ];

    let childCount = 0;
    for (const d of dirs) {
      const nx = node.state.x + d.dx;
      const ny = node.state.y + d.dy;

      if (nx >= 0 && nx < currentMaze.cols && ny >= 0 && ny < currentMaze.rows) {
        if (currentMaze.grid[ny][nx] === 0) {
          const nKey = `${nx},${ny}`;
          if (!visited.has(nKey)) {
            const nextCost = node.cost + 1;
            let priority = nextCost;

            if (algo === 'astar') {
              priority = nextCost + getManhattan({ x: nx, y: ny }, goal);
            }

            frontier.push({
              state: { x: nx, y: ny },
              path: [...node.path, { x: nx, y: ny }],
              cost: nextCost,
              priority: priority
            });
            childCount++;
          }
        }
      }
    }

    if (expandedCount % 5 === 0 || childCount > 0) {
      addLog(`Expanded (${node.state.x}, ${node.state.y}) [g=${node.cost}] ➜ Added ${childCount} successors.`);
    }

    updateTelemetry();
    drawMaze();
    return true;
  }

  function loop() {
    if (!isRunning) return;
    const canContinue = stepSearch();
    if (canContinue) {
      const delay = 420 - parseInt(speedSlider.value, 10);
      timerId = setTimeout(loop, Math.max(20, delay));
    } else {
      isRunning = false;
      playIcon.textContent = "▶";
      playText.textContent = "Start Search";
    }
  }

  btnPlay.addEventListener('click', () => {
    if (finalPath) {
      initSearch();
    }
    isRunning = !isRunning;
    if (isRunning) {
      playIcon.textContent = "⏸";
      playText.textContent = "Pause";
      simStatusBadge.textContent = "Searching...";
      loop();
    } else {
      playIcon.textContent = "▶";
      playText.textContent = "Resume";
      clearTimeout(timerId);
      simStatusBadge.textContent = "Paused";
    }
  });

  btnStep.addEventListener('click', () => {
    if (isRunning) {
      isRunning = false;
      clearTimeout(timerId);
      playIcon.textContent = "▶";
      playText.textContent = "Resume";
    }
    stepSearch();
  });

  btnReset.addEventListener('click', () => {
    initSearch();
  });

  algoSelect.addEventListener('change', () => {
    updateSimulatorAttribution();
    initSearch();
  });

  mazeSelect.addEventListener('change', () => {
    initSearch();
  });

  function drawMaze() {
    const w = canvas.width;
    const h = canvas.height;
    ctx.clearRect(0, 0, w, h);

    const cellW = w / currentMaze.cols;
    const cellH = h / currentMaze.rows;

    for (let r = 0; r < currentMaze.rows; r++) {
      for (let c = 0; c < currentMaze.cols; c++) {
        const isWall = currentMaze.grid[r][c] === 1;
        const x = c * cellW;
        const y = r * cellH;

        if (isWall) {
          ctx.fillStyle = "#0c152c";
          ctx.fillRect(x, y, cellW, cellH);
          ctx.strokeStyle = "rgba(59, 130, 246, 0.4)";
          ctx.lineWidth = 1;
          ctx.strokeRect(x + 0.5, y + 0.5, cellW - 1, cellH - 1);
        } else {
          ctx.fillStyle = "#050204";
          ctx.fillRect(x, y, cellW, cellH);
        }
      }
    }

    ctx.fillStyle = "rgba(168, 85, 247, 0.35)";
    for (const key of visited) {
      const [vx, vy] = key.split(',').map(Number);
      ctx.fillRect(vx * cellW + 1, vy * cellH + 1, cellW - 2, cellH - 2);
    }

    ctx.fillStyle = "rgba(16, 185, 129, 0.5)";
    ctx.strokeStyle = "#10b981";
    ctx.lineWidth = 1.5;
    for (const item of frontier) {
      const fx = item.state.x * cellW;
      const fy = item.state.y * cellH;
      ctx.fillRect(fx + 2, fy + 2, cellW - 4, cellH - 4);
      ctx.strokeRect(fx + 2, fy + 2, cellW - 4, cellH - 4);
    }

    if (finalPath && finalPath.length > 0) {
      ctx.beginPath();
      ctx.strokeStyle = "#f59e0b";
      ctx.lineWidth = Math.max(3, cellW * 0.35);
      ctx.lineCap = "round";
      ctx.lineJoin = "round";

      for (let i = 0; i < finalPath.length; i++) {
        const px = finalPath[i].x * cellW + cellW / 2;
        const py = finalPath[i].y * cellH + cellH / 2;
        if (i === 0) ctx.moveTo(px, py);
        else ctx.lineTo(px, py);
      }
      ctx.stroke();

      ctx.strokeStyle = "rgba(251, 191, 36, 0.3)";
      ctx.lineWidth = Math.max(7, cellW * 0.7);
      ctx.stroke();
    }

    const gx = currentMaze.goal.x * cellW + cellW / 2;
    const gy = currentMaze.goal.y * cellH + cellH / 2;
    ctx.beginPath();
    ctx.arc(gx, gy, Math.min(cellW, cellH) * 0.38, 0, Math.PI * 2);
    ctx.fillStyle = "#ef4444";
    ctx.shadowColor = "#ff2a55";
    ctx.shadowBlur = 10;
    ctx.fill();
    ctx.shadowBlur = 0;

    const pacPos = activeCurrentNode ? activeCurrentNode.state : currentMaze.start;
    const px = pacPos.x * cellW + cellW / 2;
    const py = pacPos.y * cellH + cellH / 2;
    const radius = Math.min(cellW, cellH) * 0.42;

    ctx.beginPath();
    ctx.arc(px, py, radius, 0.25 * Math.PI, 1.75 * Math.PI);
    ctx.lineTo(px, py);
    ctx.fillStyle = "#facc15";
    ctx.shadowColor = "#facc15";
    ctx.shadowBlur = 8;
    ctx.fill();
    ctx.shadowBlur = 0;
  }

  // =========================================================================
  // 7. TEAM ARCHITECTURE TOUR & RESET
  // =========================================================================
  const btnQuickTour = document.getElementById('btnQuickTour');
  const btnResetDemo = document.getElementById('btnResetDemo');

  btnQuickTour.addEventListener('click', () => {
    document.getElementById('section-team-workload').scrollIntoView({ behavior: 'smooth' });

    // Step 1: Member 1
    setTimeout(() => applyMemberFocus('m1'), 400);

    // Step 2: Member 2
    setTimeout(() => applyMemberFocus('m2'), 2400);

    // Step 3: Member 3
    setTimeout(() => applyMemberFocus('m3'), 4400);

    // Step 4: Member 4
    setTimeout(() => applyMemberFocus('m4'), 6400);

    // Step 5: All Overview & Simulator
    setTimeout(() => {
      applyMemberFocus('all');
      document.getElementById('section-simulator').scrollIntoView({ behavior: 'smooth' });
      mazeSelect.value = 'small';
      algoSelect.value = 'ucs';
      initSearch();
      setTimeout(() => btnPlay.click(), 600);
    }, 8400);
  });

  btnResetDemo.addEventListener('click', () => {
    applyMemberFocus('all');
    mazeSelect.value = 'medium';
    algoSelect.value = 'bfs';
    initSearch();
    document.getElementById('section-dashboard').scrollIntoView({ behavior: 'smooth' });
  });

  // Default initial load: All Members view with BFS active
  applyMemberFocus('all');
});
