# Games Module - Gamifikace a výukové hry

## 📋 Účel
Interaktivní vzdělávací hry pro výuku AWJ technologie

## 🎯 Herní módy

### 1. Parameter Challenge
- Uživatel musí nastavit správné parametry pro daný materiál
- Body za přesnost a rychlost
- Postupná obtížnost

### 2. Cost Optimization Game
- Minimalizovat náklady při zachování kvality
- Ekonomická simulace
- Leaderboard

### 3. Virtual AWJ Simulator
- Simulace reálného řezání
- Vizuální feedback
- Učení z chyb

### 4. Quiz Mode
- Otázky o AWJ technologii
- Různé obtížnosti
- Certifikace

## 📁 Budoucí struktura:
```
games/
├── GamesModule.jsx
├── components/
│   ├── ParameterChallenge/
│   │   ├── ChallengeGame.jsx
│   │   ├── ScoreBoard.jsx
│   │   └── Timer.jsx
│   ├── Simulator/
│   │   ├── VirtualAWJ.jsx
│   │   └── SimulationControls.jsx
│   ├── Quiz/
│   │   ├── QuizGame.jsx
│   │   └── QuestionCard.jsx
│   └── Leaderboard/
│       └── GlobalLeaderboard.jsx
├── gameLogic/
│   ├── scoring.js
│   ├── challenges.js
│   └── achievements.js
└── gamesAPI.js
```

## 📝 Příklad Challenge Game:
```jsx
const ParameterChallenge = () => {
  const [challenge, setChallenge] = useState({
    material: 'steel',
    thickness: 10,
    targetSpeed: 150  // mm/min
  });
  const [userParams, setUserParams] = useState({});
  const [score, setScore] = useState(0);

  const checkSolution = () => {
    const actualSpeed = calculateSpeed(userParams);
    const accuracy = Math.abs(actualSpeed - challenge.targetSpeed);
    const points = Math.max(0, 100 - accuracy);
    setScore(score + points);
  };

  return (
    <div className="challenge">
      <h3>Nastavte parametry pro dosažení rychlosti {challenge.targetSpeed} mm/min</h3>
      <ParameterInputs onChange={setUserParams} />
      <button onClick={checkSolution}>Zkontrolovat</button>
      <div>Skóre: {score}</div>
    </div>
  );
};
```

## 🏆 Achievement systém:
- Novice Calculator (10 výpočtů)
- Speed Master (optimalizace na rychlost)
- Cost Saver (optimalizace na náklady)
- AWJ Expert (všechny výzvy splněny)

## 💾 Backend integrace:
- Ukládání skóre
- Leaderboard
- Progress tracking

## ⚠️ Status: 🚧 PŘIPRAVENO - Čeká na implementaci
