function processData(input) {
    const lines = input.split('\n');
    const peopleCount = parseInt(lines.shift(),10);
    const bosses = new Map();
        const profits = new Map();
    for(let i=0; i<peopleCount; i++) {
        const [person, boss, percent] = lines.shift().split(' ');
        bosses.set(person, {boss, percent: parseInt(percent,10)/100})
        profits.set(person, 0);
        profits.set(boss, 0);
    }

    const sales = parseInt(lines.shift(), 10);


    profits.set('Jude', 0);

    for(let i=0; i<sales; i++) {
        const sale = lines.shift().split(' ');
        let amount = parseInt(sale[1], 10);
        const person = sale[0];
        const percents = [{person, amount:0}];

        let current = person;
        while(bosses.has(current)) {
            const boss = bosses.get(current);
            if(boss) {
                percents.push({person:boss.boss, amount:boss.percent});
                current = boss.boss;
            }
        }

        percents.reverse();

        for(const p of percents) {
            profits.set(p.person, profits.get(p.person) + (amount * (1-p.amount)));
            amount = (amount * (p.amount));
        }
    }

    const profitKeys = [...profits.keys()]
    profitKeys.sort()

    profitKeys.forEach((profitKey) => {
        console.log(`${profitKey} ${Math.round(profits.get(profitKey))}`);
    });
}

process.stdin.resume();
process.stdin.setEncoding("ascii");
_input = "";
process.stdin.on("data", function (input) {
    _input += input;
});

process.stdin.on("end", function () {
   processData(_input);
});
