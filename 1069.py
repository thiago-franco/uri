casos = int(input())
i = 0
while i < casos:    
    mine = input()
    mine = mine.replace('.','')
    shards = ['.']
    diamonds = 0
    for shard in mine:
        shards.append(shard)
        if shards[len(shards)-1] == '>' and shards[len(shards)-2] == '<':
            shards.pop(len(shards)-2)
            shards.pop(len(shards)-1)
            diamonds = diamonds + 1
    print(diamonds)
    i = i + 1
        
    
