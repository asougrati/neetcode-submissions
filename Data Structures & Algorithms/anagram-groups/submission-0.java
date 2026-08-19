class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> result = new HashMap<>();
        for (String str : strs) {
            char[] chars = str.toCharArray();
            Arrays.sort(chars);
            String current = new String(chars);
            result.putIfAbsent(current, new ArrayList<>());
            result.get(current).add(str);
        }
        return new ArrayList<>(result.values());
    }
}
