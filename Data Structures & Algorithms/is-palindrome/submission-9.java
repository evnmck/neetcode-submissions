class Solution {
    public boolean isPalindrome(String s) {

        String cleaned = s.toLowerCase().replaceAll("[^a-z0-9]", "");

        int start = 0;
        int end = cleaned.length() - 1;

        while (start <= end) {
            if (cleaned.charAt(start) != cleaned.charAt(end)){
                return false;
            }

            start++;
            end--;
        }

        return true;
    }
}
