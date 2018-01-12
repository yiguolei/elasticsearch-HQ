__author__ = 'royrusso'
import json

import jmespath


class TestCluster_v6:
    def test_get_cluster_summary(self, fixture):
        fixture.add_all_clusters(clear_first=True)

        response = fixture.app.get('/api/clusters/%s/_summary' % fixture.cluster_v6_name)

        assert 200 == response.status_code
        res = fixture.get_response_data(response)
        assert fixture.has_all_keys(fixture.config.KEYS_CLUSTER_SUMMARY, res['data'][0].keys()) is True

    def test_get_cluster_health(self, fixture):
        fixture.add_all_clusters(clear_first=True)

        response = fixture.app.get('/api/clusters/%s/_health' % fixture.cluster_v6_name)

        assert 200 == response.status_code
        res = fixture.get_response_data(response)
        assert len(res['data']) > 0

        assert fixture.has_all_keys(fixture.config.KEYS_CLUSTER_HEALTH, res['data'][0].keys()) is True

    def test_get_cluster_state(self, fixture):
        fixture.add_all_clusters(clear_first=True)

        response = fixture.app.get('/api/clusters/%s/_state' % fixture.cluster_v6_name)

        assert 200 == response.status_code
        res = fixture.get_response_data(response)
        assert fixture.has_all_keys(fixture.config.KEYS_CLUSTER_STATE, res['data'][0].keys()) is True

    def test_get_cluster_stats(self, fixture):
        fixture.add_all_clusters(clear_first=True)

        response = fixture.app.get('/api/clusters/%s/_stats' % fixture.cluster_v6_name)

        assert 200 == response.status_code
        res = fixture.get_response_data(response)
        assert fixture.has_all_keys(fixture.config.KEYS_CLUSTER_STATS, res['data'][0].keys()) is True

    def test_get_cluster_pending_tasks(self, fixture):
        fixture.add_all_clusters(clear_first=True)

        response = fixture.app.get('/api/clusters/%s/_pending_tasks' % fixture.cluster_v6_name)

        assert 200 == response.status_code
        res = fixture.get_response_data(response)
        assert fixture.has_all_keys(fixture.config.KEYS_CLUSTER_PENDING_TASKS, res['data'][0].keys()) is True

    def test_get_cluster_settings(self, fixture):
        fixture.add_all_clusters(clear_first=True)

        response = fixture.app.get('/api/clusters/%s/_settings' % fixture.cluster_v6_name)

        assert 200 == response.status_code
        res = fixture.get_response_data(response)
        assert fixture.has_all_keys(fixture.config.KEYS_CLUSTER_SETTINGS, res['data'][0].keys()) is True

    def test_put_cluster_settings(self, fixture):
        fixture.add_all_clusters(clear_first=True)

        body = {
            "transient": {
                "discovery.zen.minimum_master_nodes": 1
            }
        }

        response = fixture.app.put('/api/clusters/%s/_settings' % fixture.cluster_v6_name, data=json.dumps(body))
        assert 200 == response.status_code

        response = fixture.app.get('/api/clusters/%s/_settings' % fixture.cluster_v6_name)
        assert 200 == response.status_code
        res = fixture.get_response_data(response)
        assert jmespath.search("transient.discovery.zen.minimum_master_nodes", res['data'][0]) == "1"
