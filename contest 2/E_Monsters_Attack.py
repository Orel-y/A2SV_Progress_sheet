test_cases = int(input())
# n = monster
# k = bullet
dead = False

for _ in range(test_cases):
    for _ in range(3):
        my_position = 0
        n, k = map(int, input().split())
        monster_health = list(map(abs(int), input().split()))
        monster_dist = list(map(int, input().split()))
        dist_health_dict = {}

        for i in range(0, n):
            dist_health_dict[monster_dist[i]] = monster_health[i]
        
        #first kill the moster which is closest to my position
        while not dead:
            closest_moster = min(dist_health_dict.keys())
            if dist_health_dict[closest_moster] >= k:
                dist_health_dict[closest_moster] = dist_health_dict[closest_moster] - k

            elif dist_health_dict[closest_moster] < k:
                dist_health_dict[closest_moster] = dist_health_dict[closest_moster] - 1
        

