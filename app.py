# reval_lane2 CHECKGATE fixture - authorized CodeRabbit VDP, deliberately unsafe sample for gate-differential test
DEMO_API_TOKEN = "fixture_dummy_not_a_real_secret"

def get_user(uid):
    query = "SELECT * FROM users WHERE id = " + uid  # unsafe concat (fixture)
    return query
